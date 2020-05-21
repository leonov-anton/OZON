import re
import random

class User:

    """
    Класс данных пользователей системы

    """


    def __init__(self, login, password):

        """
        Инициализация атребутов класса

        :param login: Логин в системе.

        Должен содержать только латинские буквы загалвные или строчные,
        а так же символы: '-', '_', '.'.
        Должен содержать не менее 6и символов в любой комбинации.
        :param password: Пароль для входа в систему.

        Должен содержать только латинские буквы, цифры,
        а так же симполы: '!', '@', '#', '$', '%', '^', '&', '*'.
        Должен содердать не менее одной заглавной буквы, одной строчной, а так же одной цифры.
        Должен иметь от 6и до 26и символов.

        :param email: Почта пользователя системы.

        """

        self.login = login
        self.password = password
        # self.email = email


    def greet(self):

        """
        Проверка зарегистрирован ли пользователь в системе.
        В случае отсутствия регистрация.

        :return: Добавляет в список логин и пароль пользователя.

        """

        file_name = ''
        for i in range(7):
            file_name += random.choice('abcdefghijklmnopqrstuvwxyz')
        qest = input("Вы разерестрированный в системе? (Да/Нет): " '\n').capitalize()
        if qest == 'Да':
            # Проверить есть ли в списке логин и пароль, а пока так
            print("Супер!")
            pass
        elif qest == 'Нет':
            verif_login = re.match(r"^[a-zA-Z0-9_\.\-]{5,20}", self.login)
            verif_pass = re.match(r"(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,26}", self.password)
            if verif_login and verif_pass:
                users_list = open(file_name+'.txt', 'a', encoding='utf-8')
                users_list.write(self.login + ', ' + self.password + '\n')
                users_list.close()
                print("Вы успешно зарегистрировались")
                pass
            else:
                print("Что-то не то ввели")

    # !!!НЕ ПОЛУЧАЕТСЯ В МЕТОДЕ greet обратиться к этим методам!!!

    # def verif(self, login):
    #     if re.match(r"^[a-zA-Z0-9_\.\-]{5,20}", self.login):
    #         return login
    #     print("Ваш логин не соответствует правилам")
    #
    #
    # def verif_password(self, user_password):
    #     if re.match("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,26}", self.password):
    #         return user_password
    #     print("Ваш пароль не соответствует правилам")


