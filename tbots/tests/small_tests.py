import re
from datetime import datetime, timedelta, timezone
from dateutil import tz
import time
import pytz
from timezonefinder import TimezoneFinder

utc = tz.tzutc()

# a = {'first': 1, 'second': 2}
#
# a['third'] = 3
#
# print(a)
# #
# # a['third'] = 33
# #
# # print(a)
#
# b = a.pop('first')
#
# print(b)
#
# print(a)
#
#
# stroka = 'fshkjdf 234 dsfkhdkj rts'
#
# pattern = '1'
#
# a = re.search(pattern, stroka)
#
# if a:
#     print(a.group(0))
# else:
#     print(type(a))



tf = TimezoneFinder()
longitude = int(37.625817)
latitude = int(55.79288)
# local_tz = datetime.now(pytz.timezone(tf.certain_timezone_at(lng=longitude, lat=latitude))).strftime('%Z%z')
local_tz = pytz.timezone(tf.certain_timezone_at(lng=longitude, lat=latitude))
print(type(local_tz))
print(local_tz)
print('\n _____ \n')

needing_time = datetime(2020, 8, 11, 11, 35, tzinfo=local_tz)

needing_time_utc = datetime(2020, 8, 11, 11, 35, tzinfo=local_tz).astimezone(utc)

f_time = datetime(2020, 11, 11, 11, 35).astimezone(utc)

f_time_utc = datetime(2020, 11, 11, 11, 35).astimezone(local_tz)

print(datetime.now().astimezone(local_tz))
print(datetime.now().astimezone(utc))

print('\n _____ \n')

print(needing_time)
print(needing_time_utc)

print('\n _____ \n')

print(f_time)
print(f_time_utc)

# a = datetime.now() + timedelta(days=1)
#
# print(a)
# print(datetime.now())