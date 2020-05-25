import unittest
from Calc import Calculator


class CalcTesting(unittest.TestCase):
    """
    Tests for Calculator
    """

    def setUp(self):
        self.my_calculation = Calculator("1", "1")

    def number_input_testing(self):
        self.assertEqual(self.my_calculation.addition(), 2)

    def text_input_testing(self):
        self.assertFalse(self.my_calculation.verif_numb("sfsd"))

    def epmty_input_testing(self):
        self.assertFalse(self.my_calculation.verif_numb(""))


unittest.main()
