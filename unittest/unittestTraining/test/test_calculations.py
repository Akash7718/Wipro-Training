import unittest

from unittestTraining.src.calculations import add, sub, mul, div, ne

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10,5)
        self.assertEqual(15, res,msg='Addition error')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(5, res, msg='Substraction error')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(50, res, msg='Multiplication error')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(2.0, res, msg='Division error')
    @unittest.skip
    def test_ne(self):
        res = ne(10,10)
        self.assertTrue(res, msg='NE')

    def test_driver(self):
        with self.assertRaises(ZeroDivisionError,msg = "No Exc"):
            div(10,0)