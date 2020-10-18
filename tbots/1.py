import time
import re
from datetime import datetime, timedelta, timezone
import pytz
from dateutil import tz


# a = {'первое': 123, 'второе': 456, 'третье': 789}
# b = a.keys()
# c = []
# for i in b:
#     c.append(i)
# print(c)


# n = 1
# stroka = ''
# for i in a.keys():
#     b = f'{n}. '
#     stroka += b + i.capitalize()
#     stroka += '\n'
#     n += 1
#
# print(stroka)

utc = tz.tzutc()
# t = 1596929544
# a = datetime.fromtimestamp(t)
#
# print(datetime.now())
# b = datetime.timestamp(datetime.now().astimezone(utc))


# i = 'вынести мусор в 16:00'
#
# a = re.search(r'(\d\d)(:)(\d\d)', i)
# b = a.group(0)
#
# todo_time = b.split(':')
# time_now = time.localtime()
#
# print(todo_time)

# a = datetime.datetime(2020, 7, 20, 12, 0)
# print(a)
#
# s = ['21.07', 'в', '18:53', 'вынести', 'мусор']
#
# a = ''
# for i in s:
#     a += i
#
# print(a)


# msc = timezone(timedelta(hours=-3))
#
# time_now = datetime(2020, 7, 20, 22, 38)
#
# # print(datetime.utcnow())
# #
# # print(datetime.now())
#
# time_now1 = datetime(2020, 7, 20, 22, 38)
#
# print(time_now)

# utc = tz.tzutc()
# local = tz.tzlocal()
#
# # utc_now = datetime.now()
# utc_now = datetime(2020, 7, 20, 1, 40)
#
# # print(utc_now)
# #
# # utc_now = utc_now.replace(tzinfo=local)
# #
# # print(utc_now)
#
# local_now = utc_now.astimezone(utc)
#
# print(local_now)


# a = 'Ghbdtn'
#
# print(len(a))
#
# task_date = ['25', '7']
#
# if len(task_date[2]) == 4:
#     print('1')
# elif len(task_date) == 3 and len(task_date[2]) == 2:
#     print('2')
# else:
#     print('3')

#
# 'date': 1596928428


a = {'try': 1, 'red': 2, 'blue': 3}

for i in a:
    if i != 'try':
        print(i)

