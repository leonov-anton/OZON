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
        f = open('operation_log.json', 'a')
        if self.verif_x() and self.verif_y():
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
                json.dump(r, f)
            elif self.operation == "кор":
                if self.verif_neg_x():
                    r = 1
                    for i in range(10):
                        r = (r + (float(self.first) / r)) / 2
                    json.dump(r, f)
                print("Я не умею брать корень отрицательного числа")
        elif self.verif_x():
            print("Значение Y не число")
        else:
            print("Значение X не число")


    def verif_x(self):
        if re.match("^(-)*[0-9]+(\.)*[0-9]*", self.first):
            return True
        return False


    def verif_y(self):
        if re.match("^(-)*[0-9]+(\.)*[0-9]*", self.second):
            return True
        return False


    def verif_neg_x(self):
        if re.match("^[0-9]+(\.)*[0-9]*", self.first):
            return True
        return False