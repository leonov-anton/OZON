import requests
import json
import timezonefinder


# req = requests.get('http://api.geonames.org/timezoneJSON?lat=47.01&lng=10.2&username=demo')
# req = req.json()
# print(req)


from timezonefinder import TimezoneFinder

TimezoneFinder.using_numba()  # this is a static method returning True or False

tf = TimezoneFinder()
# tf = TimezoneFinder(in_memory=True) # to use the faster "in-memory" mode
# tf = TimezoneFinder(bin_file_location='path/to/files') # to use data files from another location

longitude, latitude = 13.358, 52.5061
print(tf.timezone_at(lng=55.028395, lat=61.646646))  # returns 'Europe/Berlin'
print(tf.certain_timezone_at(lng=longitude, lat=latitude))  # returns 'Europe/Berlin'