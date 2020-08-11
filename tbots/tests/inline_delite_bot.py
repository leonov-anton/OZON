# - *- coding: utf- 8 - *-

import logging
import re
import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from datetime import datetime, timedelta, timezone
from dateutil import tz
import time
import pytz
from timezonefinder import TimezoneFinder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    btn = [[KeyboardButton('help'), KeyboardButton('todo list')]]
    name = update.message.from_user['first_name']
    msg = f'Привет, {name}! Я бот который поможет не забыть о твоих планах. ⏰ \n\n' \
          'Напиши сообщение которое содержит время в формате ЧЧ:ММ чтобы добавить напоминание на сегодня.\n' \
          'Или укажи дату в формета ДД.ММ.ГГ. Или можно написать в сообщении "завтра" так же указав время или ' \
          'напиши в какой ближайший день недели. \n' \
          'Я пришлю тебе сообщение в указанное время.🔖\n' \
          'Написав todo list можно просматривать и управлять своими напоминаниями. 📝\n' \
          'Напиши help если захочешь прочитать это сообщение снова.\n\n' \
          'Если не хочется писать, можно нажать на кнопки ниже.'
    markup = ReplyKeyboardMarkup(btn, one_time_keyboard=False, resize_keyboard=True)
    update.message.reply_text(msg, reply_markup=markup)
    print(update.message.date)


def todo_list_view(update, context):

    todo_list_msg = ''
    number = 1

    test = {'first': 'first', 'second': 'second', 'third': 'third'}

    for i in test:
        if i != 'local_tz':
            todo_list_msg += f'{number}. {i.capitalize()}\n'
            number += 1

    if test:
        # keyboard = [[InlineKeyboardButton("🗑 Удалить", callback_data='0')]]
        # reply_markup = InlineKeyboardMarkup(keyboard)
        #
        # update.message.reply_text(text=f'{todo_list_msg}\n'
        #                                    '🗑 Чтобы удалить задачу напиши /unset <номер в списке>',
        #                               reply_markup=reply_markup)
        btn = [[KeyboardButton('🗑 Удалить')]]
        markup = ReplyKeyboardMarkup(btn, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('🗑 Чтобы удалить задачу напиши /unset <номер в списке>', reply_markup=markup)


# def test(update, context):
#     query = update.callback_query
#     query.answer()
#     print(query.data)
#     query.edit_message_text(text="Укажите номера задач которые вы хотите удалить")


def test(update, context):
    update.message.reply_text("Вызвалось")



def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text("todo list"), todo_list_view, pass_chat_data=True))
    # dp.add_handler(CallbackQueryHandler(test))
    dp.add_handler(MessageHandler(Filters.text('🗑 Удалить'), test, pass_chat_data=True))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()