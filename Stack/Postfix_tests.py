from Postfix import calculate
from unittest import TestCase

class PostfixTest(TestCase):
    def test(self):
        self.assertEqual(59, calculate('8 2 + 5 * 9 + =')) # (8 + 2)*5 + 9 = 59
        self.assertEqual(9, calculate('1 2 + 3 * =')) # (1 + 2)*3 = 9
        self.assertEqual(10, calculate('1 2 + 3 + 4 + =')) # 1 + 2 + 3 + 4 = 10
        self.assertEqual(24, calculate('1 2 * 3 * 4 * =')) # 1 * 2 * 3 * 4 = 24
        self.assertEqual(43, calculate('1 2 + 3 * 4 + 5 6 * + =')) # (1 + 2)* 3 + 4 + 5 * 6 = 9 + 4 + 30 = 43
        self.assertEqual(63, calculate('1 2 + 3 * 4 5 + 6 * + =')) # (1 + 2)*3 + (4 + 5)*6 = 9 + 54 = 63
        self.assertEqual(17, calculate('3 4 + 5 2 * + ='))
        # self.assertEqual(10, calculate('1 2 +')) -> return exeption
        
