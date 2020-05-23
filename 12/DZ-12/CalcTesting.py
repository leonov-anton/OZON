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



    def add_test(self):
        """
        Addition func test
        :return:
        """

