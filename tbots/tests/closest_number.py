import logging
import re
import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from datetime import datetime, timedelta, timezone
from dateutil import tz
import time


# l = [5, 78, 45, 12, 56, 9999]
#
# def nearest(lst, target):
#   return min(lst, key=lambda x: abs(x-target))
#
# print(nearest(l, 52))

from datetime import datetime
import pytz
# a = datetime.now(pytz.timezone('America/Chicago')).strftime('%Z%z')
# print(a)

timer = 1596373942
a = time.ctime(timer)
print(a)

# dt = datetime.strptime(timer, "%d/%m/%y %H:%M")
# print(dt)

# utc = tz.tzoffset('+3', -10800)
# # utc = tz.tzutc()
# time_now = datetime.now()

# task_time = datetime(int(2020), int(8), int(2), int(3), int(15),
#                      tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
# time_now = time_now.astimezone(utc)
#
# print(time_now)
# print(task_time)
#
# print(time_now)

# time_now = datetime.now().astimezone(utc)
# print(time_now)
