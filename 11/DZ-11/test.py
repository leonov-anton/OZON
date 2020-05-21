from User import *

user_login = input("Введите логин: " '\n')
user_password = input("Введите пароль: " '\n')

user1 = User(user_login, user_password)

user1.greet()