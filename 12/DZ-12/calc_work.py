from Calc import Calculator

x = input("Введите первое число: ")
oper = input("Введите знак операции: ")
y = input("Введите второе число: ")

work = Calculator(x, oper, y)

print(work.count())