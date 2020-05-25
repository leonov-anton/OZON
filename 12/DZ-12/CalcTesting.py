import unittest
from Calc import Calculator


class CalculatorTesting(unittest.TestCase):
    """
    Tests for Calculator
    """

    def setUp(self):
        x = 5
        y = 3
        self.my_calculation = Calculator(x, y)

    def number_input_testing(self):
        self.my_calculation.verif_numb('5')
        self.assertEqual(self.my_calculation.verif_numb('5'), True)

    def text_input_testing(self):
        self.my_calculation.verif_numb('safdsf')
        self.assertFalse(self.my_calculation.verif_numb('safdsf'))

    def epmty_input_testing(self):
        self.my_calculation.verif_numb('')
        self.assertFalse(self.my_calculation.verif_numb(''))


unittest.main()
