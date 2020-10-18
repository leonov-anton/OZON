# - *- coding: utf- 8 - *-

import logging
from sqliter import SQLighter
import re
import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from datetime import datetime, timedelta, timezone

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

def add_contact(update, context):
    name = f'{update.message.contact.last_name} {update.message.contact.first_name}'
    phone = update.message.contact.phone_number
    if phone[0] == '7':
        phone = phone.replace('7', '8', 1)
    if update.message.contact.vcard:
        email = re.search(r'[a-zA-Z0-9_\.\-]+@\w+[-_]?\w+\.\w+', update.message.contact.vcard)
        db = SQLighter('phonelist.db')
        db.add_contact(Name=name, Phone_1=phone, EMail=email.group(0))
        update.message.reply_text("Я получил контакт")
        db.close()
    else:
        db = SQLighter('phonelist.db')
        db.add_contact(Name=name, Phone_1=phone)
        update.message.reply_text("Я получил контакт")
        db.close()


def get_contact(update, context):
    db = SQLighter('phonelist.db')
    update.message.reply_text(
        db.get_names(update.message.text)[0][0] + '\n' + str(db.get_names(update.message.text)[0][1]))
    db.close()


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)

    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.contact, add_contact)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.regex('^(Age|Favourite colour|Number of siblings)$'), regular_choice
                ),
                MessageHandler(Filters.regex('^Something else...$'), custom_choice),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), regular_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')),
                    received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dp.add_handler(MessageHandler(Filters.contact, add_contact, pass_job_queue=True, pass_chat_data=True))


    dp.add_handler(MessageHandler(Filters.text, get_contact, pass_job_queue=True, pass_chat_data=True))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
