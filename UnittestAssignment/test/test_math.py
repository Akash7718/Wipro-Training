
import unittest
from src import math

#Basic Test Case
class TestMath(unittest.TestCase):
    def test_add(self):
        res = math.add(2,3)
        self.assertEqual(5,res,msg="Addition error")

#Setup and Teardown
class TestList(unittest.TestCase):
    def setUp(self):
        self.data = math.get_list()

    def tearDown(self):
        print("Test completed")

    def test_list_length(self):
        self.assertEqual(3,len(self.data),msg="List Length error")

#Multiple Assertions
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        res = math.to_upper("hello")
        self.assertEquals("HELLO",res,msg="Uppercase error")

    def test_is_upper(self):
        res  = math.is_upper("hello")
        self.assertFalse(res,msg="isupper error")


#Exception Testing
class TestException(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            math.divide(10,0)

#Test Suite Execution

class TestAdd(unittest.TestCase):
    def test_addition(self):
        res=math.add(5,5)
        self.assertEqual(10,res,msg="Addition error")

class TestSubtract(unittest.TestCase):
    def test_subtraction(self):
        res = math.subtract(10,5)
        self.assertEqual(5,res,msg="Subtraction error")

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestAdd))
    suite.addTest(unittest.makeSuite(TestSubtract))

    runner = unittest.TextTestRunner()
    runner.run(suite)
