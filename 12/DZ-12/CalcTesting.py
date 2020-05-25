import unittest
from Calc import Calculator


class CalcTesting(unittest.TestCase):
    """
    Tests for Calculator
    """

    def setUp(self):
        x = str(1)
        y = str(2)
        self.my_calculation = Calculator(x, y)

    def test_number_input_testing(self):
        self.assertEqual(self.my_calculation.addition(), 3)

    def test_text_input_testing(self):
        self.assertFalse(self.my_calculation.verif_numb("sfsd"))

    def test_epmty_input_testing(self):
        self.assertTrue(self.my_calculation.verif_numb("2"))


unittest.main()
