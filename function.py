# def greet():
#     a = 3
#     text = input()
#     print("Првиет, Мир!")
#     print(a*text)


# def printn(text, kol):
#     print(text*kol)
#
# printn("Text")


# name_of_user = input("Можете ввести свое имя: ")
# surname_of_user = input("Можете ввести свою фамилию: ")
#
#
# def get_name(name="Аноним", surname="Анонимов"):
#     print("Добрый день", name.title(), surname.title())
#
# get_name("Peter")
# get_name(name=name_of_user, surname=surname_of_user)


# def func(chislo):
#     return chislo ** chislo
# print(func(5))


# import random
#
#
# def get_name():
#     name = input("Введите ваше имя: ")
#     return name.strip().title()
#
#
# def generate_number(name_length):
#     name_length = len(name_length)
#     rand_str = ''
#     for i in range(name_length):
#         rand_num = random.randint(1, name_length)
#         rand_str += str(rand_num)
#     return rand_str
#
#
# def get_full_data():
#     name = get_name()
#     number = generate_number(name)
#     return name + " " + str(number)
#
#
# print(get_full_data())

# fname = input("Введите имя: ")
# sname = input("Введите фамилию: ")
# tname = input("Введите отчество: ")
#
# def name(firs_name, secand_name, third_name):
#     if third_name:
#         return "Привет, " + secand_name + " " + firs_name + " " + third_name
#     else:
#         return "Привет, " + firs_name + " " + secand_name
#
# print(name(fname, sname, tname))

# myList = [1, 2, 3]
#
# def myFunc(a):
#     funclist = a[:]
#     funclist.append(4)
#     return funclist
#
# print(myFunc(myList))
# print(myList)

person = {'names':[], 'surnames': []}


def create_person(name, surname):
    """Возвращает словарь с информацией о человеке"""
    person['names'].append(name)
    person['surnames'].append(surname)
    return person


user_size = int(input("Введите количество пользователей, которые должны появиться в  этом словаре: "))
for user in range(user_size):
    name = input("Введите имя пользователя: ")
    surname = input("Введите фамилию пользователя: ")
    create_person(name, surname)

print(person)