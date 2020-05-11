import re

email = input("Введите Вашу почту: ")
login = input("Введите Ваш логин: ")

users_list = open('users_list.txt', 'a', encoding='utf-8')

if re.match(r'^[a-zA-Z0-9_\.\-]+@\w+\.\w+$', email) and re.match(r'^[a-zA-Z0-9_\.\-\@]+$', login):
    users_list.write(email + ', ' + login + '\n')
elif re.match(r'^[a-zA-Z0-9_\.\-]+@\w+\.\w+$', email) is None:
    print("Вы ввели не почту")
else:
    print("Вы ввели недопустимый логин")

 users_list.close()