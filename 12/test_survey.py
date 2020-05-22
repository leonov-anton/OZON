import unittest
from survey import Survey

class TestSurvey(unittest.TestCase):
    """Тесты для класса Survey"""

    def setUp(self):
        """Создание опроса"""
        question = "Лучший язык программирования?"
        self.mysurvey = survey(question)
        self.answers = ['Rython', 'C++', 'C#']

    def test_save_single_answer(self):
        self.mysurvey.save_answer(self.answers[0])
        self.assertIn(self.answers[0], self.mysurvey.answers)

unittest.main()