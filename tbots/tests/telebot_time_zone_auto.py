import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import random
import json
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta, timezone
import pytz
from dateutil import tz



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

utc = tz.tzutc()


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def location(update, context):
    tf = TimezoneFinder()
    time_now = datetime.now()
    longitude = update.message.location['longitude']
    latitude = update.message.location['latitude']
    a = datetime.now(pytz.timezone(tf.certain_timezone_at(lng=longitude, lat=latitude))).strftime('%Z%z')
    b = pytz.timezone(tf.certain_timezone_at(lng=longitude, lat=latitude))
    print(b)
    tzzz_hours = int(a[-5:]) // 100
    tzzz_minutes = int(a[-5:]) % 100
    # due = datetime(time_now.year, time_now.month, time_now.day, 1, 2,
    #                tzinfo=timezone(timedelta(hours=int(a[-5:]) / 100)))
    # print(due)
    # task_time = datetime(time_now.year, time_now.month, time_now.day, int(1),
    #                      int(1), tzinfo=timezone(timedelta(hours=tzzz)))
    # print(task_time)
    task_time = datetime(time_now.year, time_now.month, time_now.day, int(1),
                         int(1), tzinfo=timezone(timedelta(hours=tzzz_hours, minutes=tzzz_minutes))).astimezone(utc)
    print(task_time)
    context.chat_data['local_tz'] = {'hours': tzzz_hours, 'minutes': tzzz_minutes}
    print(context.chat_data)

def tz(update, context):
    print(type(update.message.date))


# def test(update, context):
#     query = update.callback_query
#     print(query.answer())

def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)
    dp = updater.dispatcher

    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    # dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.location, location, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.text, tz, pass_job_queue=True, pass_chat_data=True))
    dp.add_error_handler(error)
    # dp.add_handler(CallbackQueryHandler(test))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
