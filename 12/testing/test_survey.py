import unittest
from survey import survey

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

    def test_save_triple_answer(self):
        for answer in self.answers:
            self.mysurvey.save_answer(answer)
        for answer in self.answers:
            self.assertIn(answer, self.mysurvey.answers)

unittest.main()