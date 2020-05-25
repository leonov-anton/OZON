from Calc import Calculator

x = input("Введите первое число (X): ")
oper = input("Введите знак операции (+, -, *, /, ^, кор): ")
if oper != "кор":
    y = input("Введите второе число (Y): ")
else:
    y = str(1)

work = Calculator(x, oper, y)

print(work.count())