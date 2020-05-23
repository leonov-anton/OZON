import re

class Calculator
    """
    Сalculator simple math functions
    
    """


    def __init__(self, x, y):
        """

        :param x: first number
        :param y: second number

        """
        self.x = 0
        self.y = 0


    def count(self):
        if self.verif_x() and self.verif_y():
            print("Что будем делать с этим?")
            oper = input("Сложение - +, вычитание - , умножение - *, деление - /, степень - ^, корень - кор: ")
            if oper == "+":
                return self.x + self.y
                pass
            elif oper == "-":
                return self.x - self.y
                pass
            elif oper == "*":
                return self.x * self.y
                pass
            elif oper == "/":
                return self.x / self.y
                pass
            elif oper == "^":
                for i in range(self.y):
                    r = 1
                    r = r * self.x
                return r
                pass
            elif oper == "кор":
                if self.verif_neg_x():
                    for i in range(10):
                        r = 1
                        r = (r + (self.x / r)) / 2
                    return r
                    pass
                print("Я не умею брать корень отрицательного числа")
                pass
        elif self.verif_x():
            print("Значение Y не число")
            pass
        print("Значение X не число")
        pass


    # def addition(self):
    #     r = self.x + self.y
    #
    #
    # def subtraction(self):
    #     r = self.x - self.y
    #
    #
    # def multiplication(self):
    #     r = self.x * self.y
    #
    #
    # def division(self):
    #     r = self.x / self.y
    #
    #
    # def exponentiation(self):
    #     for i in range(self.y):
    #         r = 1
    #         r = self.r * self.x
    #
    #
    # def square(self):
    #     for i in range(10):
    #         r = 1
    #         r = (self.r + (self.x / self.r)) / 2


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