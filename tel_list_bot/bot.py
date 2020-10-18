#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from sqliter import SQLighter
import re
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

ADD_EMAIL, ADD_COMPANY = range(2)

reply_keyboard = [['Закончить'],]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def add_contact(update, context):
    phone = update.message.contact.phone_number
    name = f'{update.message.contact.last_name} {update.message.contact.first_name}'

    if phone[0] == '7':
        phone = phone.replace('7', '8', 1)

    context.chat_data['phone'] = phone
    context.chat_data['name'] = name

    if update.message.contact.vcard:
        email = re.search(r'[a-zA-Z0-9_\.\-]+@\w+[-_]?\w+\.\w+', update.message.contact.vcard)
        context.chat_data['email'] = email.group(0)
        update.message.reply_text('Укажите команию для этого контакта или нажмите "Закончить"', reply_markup=markup)

        return ADD_COMPANY

    else:
        update.message.reply_text('Укажите элекронную почту, если она не известна то укажите название компании '
                                  'или нажмите "Закончить"', reply_markup=markup)

        return ADD_EMAIL


def add_email(update, context):
    email = update.message.text
    context.chat_data['email'] = email
    update.message.reply_text('Укажите команию для этого контакта или нажмите "Закончить"', reply_markup=markup)

    return ADD_COMPANY


def add_company(update, context):
    if 'email' not in context.chat_data:
        context.chat_data['email'] = 'не указана'

    company = update.message.text
    context.chat_data['company'] = company
    db = SQLighter('phonelist.db')
    db.add_contact(Name=context.chat_data['name'], Phone_1=context.chat_data['phone'],
                   EMail=context.chat_data['email'], Company=context.chat_data['company'])
    update.message.reply_text("Контакт добавлен в справочник")
    db.close()
    context.chat_data.clear()

    return ConversationHandler.END


def done(update, context):
    if 'email' not in context.chat_data:
        context.chat_data['email'] = 'не указана'
    if 'company' not in context.chat_data:
        context.chat_data['company'] = 'не указана'
    db = SQLighter('phonelist.db')
    db.add_contact(Name=context.chat_data['name'], Phone_1=context.chat_data['phone'], EMail=context.chat_data['email'],
                   Company=context.chat_data['company'])
    update.message.reply_text("Контакт добавлен в справочник")
    db.close()
    context.chat_data.clear()

    return ConversationHandler.END


def get_contact(update, context):
    db = SQLighter('phonelist.db')
    search_result = db.get_names(update.message.text) + db.get_company(update.message.text)
    db.close()

    if len(search_result) == 0:
        update.message.reply_text(f'По запросу "{update.message.text.upper()}" ничего не найдено.')

    elif len(search_result) > 1:
        msg = ''
        number = 1
        for i in search_result:
            msg += f'{number}. {i[0]} \n' \
                   f'тел: {i[1]} \n' \
                   f'комп: {i[3]} \n' \
                   f'email: {i[4]} \n \n'
            number += 1
        update.message.reply_text(msg)

    else:
        msg = f'{search_result[0][0]} \n' \
              f'тел: {search_result[0][1]} \n' \
              f'комп: {search_result[0][3]} \n' \
              f'email: {search_result[0][4]} \n \n'
        update.message.reply_text(msg)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.contact, add_contact)],
        states={
            ADD_EMAIL: [
                MessageHandler(
                    Filters.regex('^[a-zA-Z0-9_\.\-]+@\w+[-_]?\w+\.\w+$'), add_email
                ),
                MessageHandler(Filters.text & ~(
                        Filters.regex('^[a-zA-Z0-9_\.\-]+@\w+[-_]?\w+\.\w+$') | Filters.regex('^Закончить$')),
                               add_company),
            ],
            ADD_COMPANY: [
                MessageHandler(
                    Filters.text & ~(Filters.regex('^[a-zA-Z0-9_\.\-]+@\w+[-_]?\w+\.\w+$') | Filters.regex(
                        '^Закончить$') | Filters.contact), add_company
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Закончить$'), done)],
    )

    dp.add_handler(conv_handler)

    dp.add_handler(MessageHandler(Filters.text, get_contact, pass_job_queue=True, pass_chat_data=True))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
