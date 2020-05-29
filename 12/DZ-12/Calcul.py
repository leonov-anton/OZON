import re
import json


class Calculator:
    """
    Сalculator of simple math functions

    Methods 'add', 'dif', 'mult', 'div', 'exp', 'square' returns resolt of calculation
    and also save dicts to log file (json format).
    Key dist - operation, value dict - result (float).

    """

    def __init__(self, first, second):

        self.first = first
        self.second = second

    def add(self):
        """Addition x+y"""
        log = self.log_load()
        # метод log_load возвращает список, но метод списков append для функции не работает,
        # можно ли не присваивать методу переменную а как-то напрямую обращаться к списку по имени метода?
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            log.append({f"{float(self.first)} + {float(self.second)}":
                           float(self.first) + float(self.second)})
            file = open('operation_log.json', 'w')
            json.dump(log, file, indent=1, separators=', ')
            file.close()
            return float(self.first) + float(self.second)
        else:
            print("Я могу складывать только числа")

    def dif(self):
        """Difference x-y"""
        log = self.log_load()
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            log.append({f"{float(self.first)} - {float(self.second)}":
                           float(self.first) - float(self.second)})
            file = open('operation_log.json', 'w')
            json.dump(log, file, indent=1, separators=',:')
            file.close()
            return float(self.first) - float(self.second)
        else:
            print("Я могу вычитать только числа")

    def mult(self):
        """Multiplication x*y"""
        log = self.log_load()
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            log.append({f"{float(self.first)} * {float(self.second)}":
                           float(self.first) * float(self.second)})
            file = open('operation_log.json', 'w')
            json.dump(log, file, indent=1, separators=',:')
            file.close()
            return float(self.first) * float(self.second)
        else:
            print("Я могу умножать только числа")

    def div(self):
        """Division x/y"""
        log = self.log_load()
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            try:
                log.append({f"{float(self.first)} / {float(self.second)}":
                               float(self.first) / float(self.second)})
                file = open('operation_log.json', 'w')
                json.dump(log, file, indent=1, separators=',:')
                file.close()
                return float(self.first) / float(self.second)
            except ZeroDivisionError:
                print("На ноль делать нельзя")
        else:
            print("Я могу делить только числа")

    def exp(self):
        """Exponentiation x^y"""
        log = self.log_load()
        if self.verif_numb(self.first) and self.verif_numb(self.second):
            r = 1
            for i in range(int(self.second)):
                r = r * float(self.first)
            file = open('operation_log.json', 'w')
            log.append({f"{self.first} ^ {self.second}": r})
            json.dump(log, file, indent=1, separators=',:')
            file.close()
            return r
        else:
            print("Я могу возводить в степень только числа")

    def square(self):
        """Square x. Calculate by Geron method."""
        log = self.log_load()
        if self.verif_numb(self.first) and float(self.first) >= 0:
            r = 1
            for i in range(10):
                r = (r + (float(self.first) / r)) / 2
            file = open('operation_log.json', 'w')
            log.append({"sguare " + str(self.first): r})
            json.dump(log, file, indent=1, separators=',:')
            file.close()
            return r
        else:
            print("Я не умею брать корень отрицательного числа")

    def verif_numb(self, number):
        """Verification value as s number"""
        if re.fullmatch(r"^(-)?[0-9]+(\.)?[0-9]*", number):
            return True
        return False

    def last(self):
        """Return last calculation as dist:
        key - operation, value - result"""
        file = open("operation_log.json")
        log = json.load(file)
        return log[-1]

    def log_load(self):
        """ Loading Log file"""
        # не получается загрузить пустой json файл, данный метод либо добавлять пустой список в
        # json файл, если список уже был то загружает. Или можно по другому?
        try:
            file = open("operation_log.json")
            log = json.load(file)
            file.close()
            return log
        except json.decoder.JSONDecodeError:
            list = []
            file = open("operation_log.json", 'w')
            log = json.dump(list, file)
            file.close()
            log = json.load(file)
            file.close()
            return log
