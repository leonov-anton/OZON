day = int(input("day of birth: "))

try:
    if day > 31 or day < 1:
        raise ValueError("неверная дата")
except ValueError as msg:
    print(type(ValueError))
    print("Ошибка!", msg)
finally:
    print("Отличны сегодян денек")