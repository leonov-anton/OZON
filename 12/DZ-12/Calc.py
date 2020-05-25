import re
import json


class Calculator:
    """
    Сalculator of simple math functions
    
    """

    def __init__(self, first, second):

        self.first = first
        self.second = second

    def addition(self):
        """Addition x+y"""
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            json.dump(f"{float(self.first)} + {float(self.second)} = "
                      f"{float(self.first) + float(self.second)}", file)
            file.close()

    def difference(self):
        """Difference x-y"""
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            json.dump(f"{float(self.first)} - {float(self.second)} = "
                      f"{float(self.first) - float(self.second)}", file)
            file.close()

    def multiplication(self):
        """Multiplication x*y"""
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            json.dump(f"{float(self.first)} * {float(self.second)} = "
                      f"{float(self.first) * float(self.second)}", file)
            file.close()

    def division(self):
        """Division x/y"""
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second) and float(self.second) != 0:
            json.dump(f"{float(self.first)} / {float(self.second)} = "
                      f"{float(self.first) / float(self.second)}", file)
            file.close()
        else:
            print("На ноль делить нельзя")

    def exponentiation(self):
        """Exponentiation x^y"""
        # TODO negative degree
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            r = 1
            for i in range(int(self.second)):
                r = r * float(self.first)
            json.dump(f"{self.first} ^ {self.second} = {r}", file)
            file.close()

    def square(self):
        """Square x. Calculate by Geron method."""
        file = open('operation_log.json', 'a', encoding='utf-8')
        if self.verif_numb(self.first) and float(self.first) >= 0:
            r = 1
            for i in range(10):
                r = (r + (float(self.first) / r)) / 2
            json.dump("Корень из " + self.first + " = " + str(r), file)
            file.close()
        else:
            print("Я не умею брать корень отрицательного числа")

    def verif_numb(self, number):
        """Verification value as s number"""
        if re.match(r"^(-)*[0-9]+(\.)*[0-9]*", number):
            return True
        return False
