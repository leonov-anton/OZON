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

week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

week_day_dict = {i: n for i, n in zip(week, range(7))}

week_1 = ['понедель(.*)', 'вторник', 'среду', 'четверг', 'пятниц', 'суббот', 'воскресенье']

for i, n in zip(week_1, range(7)):
    week_day_dict[i] = n

looking_day = str(input('Введите день недели: '))

week_day_dict = {'пн': 0, 'вт': 1, 'ср': 2, 'чт': 3, 'пт': 4, 'сб': 5, 'вс': 6,
                 'понедель': 0, 'понедельник': 0, 'понедельн': 0, 'понедельни': 0, 'вторник': 1, 'среду': 2, 'среда': 2,
                 'четверг': 3, 'пятниц': 4, 'пятница': 4, 'пятницу': 4, 'суббот': 5, 'суббота': 5, 'субботу': 5,
                 'воскресенье': 6}


week_day_pattern = ''

for i, n in zip(week, week_1):
    week_day_pattern += str(i + '|')
    week_day_pattern += str(n + '|')

week_day_pattern = '(' + week_day_pattern[0: -1] + ')'

week_day_pattern = str(r'((\b(пн|вт|вторник|ср|чт|четверг|пт|сб|вс|воскресенье)\b)|(понедель|сред(у|a)|пятниц|суббот))')

wd = re.search(week_day_pattern, looking_day)

print(wd)

if week_day_dict[wd.group(0)] < week_day_now:
    a = 6 - week_day_now
    task_time = datetime(time_now.year, time_now.month, time_now.day, int(10)) + timedelta(days=(a + week_day_dict[wd.group(0)] + 1))
elif week_day_dict[wd.group(0)] > week_day_now:
    a = week_day_dict[wd.group(0)] - week_day_now
    task_time = datetime(time_now.year, time_now.month, time_now.day, int(10)) + timedelta(days=a)
else:
    task_time = datetime(time_now.year, time_now.month, time_now.day, int(10)) + timedelta(days=7)

print(task_time)