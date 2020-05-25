import unittest
from Calc import Calculator


class CalculatorTesting(unittest.TestCase):
    """
    Tests for Calculator
    """

    def number_input_testing(self):
        self.x = Calculator.verif_numb('5')
        self.assertEqual(self.x, True)

    def text_input_testing(self):
        self.x = Calculator.verif_numb('safdsf')
        self.assertFalse(self.x)

    def epmty_input_testing(self):
        self.x = Calculator.verif_numb('')
        self.assertFalse(self.x)

unittest.main()
