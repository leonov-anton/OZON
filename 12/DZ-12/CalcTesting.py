import unittest
from Calc import Calculator

class CalculatorTesting(unittest.TestCase):
    """
    Tests for Calculetor
    """


    def input_number_test(self):

        """
        Input number testing

        """
        myNumbers = Calculator('9', '+', '9')
        self.assert(myNumbers, '10')

unittest.main()