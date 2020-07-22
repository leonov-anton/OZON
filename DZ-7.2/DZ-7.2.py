import os
import time
import re


# def diary(text):
#     date = time.strftime("%d.%m.%Y", time.localtime())
#     file_name = str((date) + '/' + time.strftime("%H.%M %d.%m.%Y", time.localtime()) + '.txt')
#     try:
#         os.mkdir(date)
#         note = open(file_name, 'w', encoding='utf-8')
#         note.write(text)
#     except FileExistsError:
#         note = open(file_name, 'a', encoding='utf-8')
#         note.write(text)
#     note.close()
#
#
# text = input("Введите текст Вашей заметки: ")
# diary(text)

# time_now = time.localtime()
#
# print(time_now[3])
# due = ((22 * 60 + 0) * 60) - ((time_now[3] * 60 + time_now[4]) * 60 + time_now[5])
# print(due)

string = ['Позвонить', 'маме', 'в', '21:13']

for i in string:
    if re.match(r'(\d\d)(:)(\d\d)', i):
        print(i)
