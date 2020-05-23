from Calc import Calculator

x = input("Введите первое число: " '\n')
y = input("Введите второе число: " '\n')

work = Calculator(x, y)

print(work.count())