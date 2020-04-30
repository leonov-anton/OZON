def prime(number):
    for i in range(2, number):
        if number % i == 0:
            a = "не простое число"
            print("Кроме себя и единицы " + str(number) + " делится так же на " + str(i))
            break
    else:
        a = "простое число"
    print(str(number) + " " + a)

number = int(input("Введите натуральное число: "))
prime(number)