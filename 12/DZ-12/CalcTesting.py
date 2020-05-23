import unittest
from calc import calcuiator

class CalculatorTesting(unittest.TestCase):
    """
    Tests for Calculetor
    """

    def setUp(self):
        x = 9
        y = 3
        self.my_x = calcuiator(x)
        self.my_y = calcuiator(y)



    def input_number_test(self):

        """
        Input number testing

        """


