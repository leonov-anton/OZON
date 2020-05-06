while True:
    first = input()
    if first == "q":
        break
    second = input()
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("На ноль делить нельзя, алё!!!")
    except ValueError:
        print("Вы ввкли строку")
    else:
        print(answer)