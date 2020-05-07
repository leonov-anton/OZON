import os
import shutil

while True:
    choice = input("Укажите что делать? Создавать - C, Удалять - D, Выход - Q\n").upper()
    if choice == "Q":
        exit()
    elif choice == "C":
        dir_name = input("Введите название создаваемой деректории: ")
        os.mkdir(dir_name)
    elif choice == "D":
        dir_name = input("Введите название удаляемой деректории: ")
        shutil.rmtree(dir_name)