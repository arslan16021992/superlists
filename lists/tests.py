from django.test import TestCase

class SmokeTest(TestCase):
    '''смоук-тест бля'''
    def test_bad_math(self):
        self.assertEqual(1+1, 3)
