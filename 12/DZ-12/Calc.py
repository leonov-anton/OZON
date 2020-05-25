import re
import json


class Calculator:
    """
    Сalculator of simple math functions
    
    """

    def __init__(self, first, oper, second):

        self.first = first
        self.operation = oper
        self.second = second

    def count(self):
        f = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            if self.operation == "+":
                json.dump(f"{float(self.first)} + {float(self.second)} = "
                          f"{float(self.first) + float(self.second)}", f)
            elif self.operation == "-":
                json.dump(f"{float(self.first)} - {float(self.second)} = "
                          f"{float(self.first) - float(self.second)}", f)
            elif self.operation == "*":
                json.dump(f"{float(self.first)} * {float(self.second)} = "
                          f"{float(self.first) * float(self.second)}", f)
            elif self.operation == "/":
                json.dump(f"{float(self.first)} / {float(self.second)} = "
                          f"{float(self.first) / float(self.second)}", f)
            elif self.operation == "^":
                r = 1
                for i in range(int(self.second)):
                    r = r * float(self.first)
                json.dump(f"{self.first} ^ {self.second} = {r}", f)
            elif self.operation == "кор":
                if self.verif_numb(self.first) and float(self.first) > 0:
                    r = 1
                    for i in range(10):
                        r = (r + (float(self.first) / r)) / 2
                    json.dump("Корень из " + self.first + " = " + str(r), f)
                else:
                    print("Я не умею брать корень отрицательного числа")
        elif self.verif_numb(self.first):
            print("Значение Y не число")
        else:
            print("Значение X не число")

    def verif_numb(self, number):
        if re.match("^(-)*[0-9]+(\.)*[0-9]*", number):
            return True
        return False
