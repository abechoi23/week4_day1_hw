from whiteboard import *
# change whiteboard to python file name, you can change * to function name
import unittest

class CalculatorTest(unittest.TestCase):

    def test_check_lucky(self):
        result1 = check_lucky([2,2,3,4])
        self.assertEqual(result1, 2)
        result2 = check_lucky( [1,2,2,3,3,3])
        self.assertEqual(result2, 3)
        
    def test_no_luck(self):
        result = check_lucky([2,2,2,3,3])
        self.assertEqual(result, -1)

unittest.main()
