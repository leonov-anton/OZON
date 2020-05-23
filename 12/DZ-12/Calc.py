import re

class Calculator
    """
    Simple calculator
    
    """


    def __init__(self, x, y, r):
        """

        :param x: first number
        :param y: second number
        :param r: result
        """
        self.x = 0
        self.y = 0
        # self.r = 0


    def count(self):
        print("Что будем делать с этим?")
        oper = input("Сложение - +, вычитание - , умножение - *, деление - /, степень - ^, корень - кор: ")
        if oper == "+":
            self.addition()
        elif oper == "-":
            self.subtraction()
        elif oper == "*":
            self.multiplication()
        elif oper == "/":
            self.division()
        elif oper == "^":
            self.exponentiation()
        elif oper == "кор":
            self.square()


    def addition(self):
        self.y = input("Введите слогаемое: ")
        r = self.x + self.y


    def subtraction(self):
        self.y = input("Введите вычитаемое: ")
        self.r = self.x - self.y


    def multiplication(self):
        self.y = input("Введите множитель: ")
        self.r = self.x * self.y


    def division(self):
        self.y = input("Введите делитель: ")
        self.r = self.x / self.y


    def exponentiation(self):
        self.y = input("Введите степень: ")
        for i in range(self.y):
            self.r = 1
            self.r = self.r * self.x


    def square(self):
        for i in range(10):
            self.r = 1
            self.r = (self.r + (self.x / self.r)) / 2


    def verif_x(self):
        if re.match(r"(-)*[0-9]+(\.)*[0-9]*", self.x)
            return True
        return False


    def verif_y(self):
        if re.match(r"(-)*[0-9]+(\.)*[0-9]*", self.y)
            return True
        return False


    def verif_neg_x(self):
        if re.match(r"[0-9]+(\.)*[0-9]*", self.x)
            return True
        return False