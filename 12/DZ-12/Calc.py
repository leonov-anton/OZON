import re
import json

class Calculator:

    """
    Сalculator of simple math functions
    
    """


    def __init__(self, first, second):

        self.first = first
        self.second = second


    def count(self):
        f = open('operation.json', 'a')
        if self.verif_x() and self.verif_y():
            print("Что будем делать с этим?")
            oper = input("Сложение - +, вычитание - , умножение - *, деление - /, степень - ^, корень - кор: ")
            if oper == "+":
                json.dump(f"{float(self.first)} + {float(self.second)} = "
                          f"{float(self.first) + float(self.second)}", f)
                pass
            elif oper == "-":
                json.dump(f"{float(self.first)} - {float(self.second)} = "
                          f"{float(self.first) - float(self.second)}", f)
                pass
            elif oper == "*":
                json.dump(f"{float(self.first)} * {float(self.second)} = "
                          f"{float(self.first) * float(self.second)}", f)
                pass
            elif oper == "/":
                json.dump(f"{float(self.first)} / {float(self.second)} = "
                          f"{float(self.first) / float(self.second)}", f)
                pass
            elif oper == "^":
                r = 1
                for i in range(int(self.second)):
                    r = r * float(self.first)
                json.dump(r, f)
                pass
            elif oper == "кор":
                if self.verif_neg_x():
                    r = 1
                    for i in range(10):
                        r = (r + (float(self.first) / r)) / 2
                    json.dump(r, f)
                    pass
                print("Я не умею брать корень отрицательного числа")
                pass
        elif self.verif_x():
            print("Значение Y не число")
            pass
        print("Значение X не число")
        pass


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