import re
import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from datetime import datetime, timedelta, timezone
from dateutil import tz
import pytz
from timezonefinder import TimezoneFinder

time_now = datetime.now()
week_day_now = time_now.weekday()

week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

week_day_dict = {i: n for i, n in zip(week, range(0, 6))}

# looking_day = str(input())


if week_day_dict['mon'] < week_day_now:
    a = 6 - week_day_now
    task_time = time_now + timedelta(days=(a + week_day_dict['mon'] + 1))
elif week_day_dict['mon'] > week_day_now:
    a = week_day_dict['mon'] - week_day_now
    task_time = time_now + timedelta(days=a)
else:
    task_time = time_now + timedelta(days=7)