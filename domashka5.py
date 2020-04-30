# def prime(number):
#     number = int(input("Введите натуральное число: "))
#     if number <= 0:
#         number = int(input("Вы ввели не натуральное число, попробуйте еще раз: "))
#     elif

number = int(input("Введите натуральное число: "))
for i in range(2, number):
    if number % i == 0:
        print("не простое")
        break
else:
    print("простое")