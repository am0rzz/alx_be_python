import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):
    """
    Test Cases for the Simple Calculator.
    """
    def test_add(self):
        self.assertEqual(SimpleCalculator().add(5,5), 10)
        self.assertEqual(SimpleCalculator().add(2,3), 5)
        self.assertEqual(SimpleCalculator().add(-1,1), 0)
    
    def test_subtract(self):
        self.assertEqual(SimpleCalculator().subtract(5,2), 3)
        self.assertEqual(SimpleCalculator().subtract(3,2), 1)
        self.assertEqual(SimpleCalculator().subtract(-1,1), -2)
    
    def test_multiply(self):
        self.assertEqual(SimpleCalculator().multiply(5,2), 10)
        self.assertEqual(SimpleCalculator().multiply(4,3), 12)
        self.assertEqual(SimpleCalculator().multiply(1,2), 2)
    
    def test_divide(self):
        self.assertEqual(SimpleCalculator().divide(5,5), 1)
        self.assertIsNone(SimpleCalculator().divide(10,0))

if __name__ == '__main__':
    unittest.main()

# if the main fuction Raised Zero Divison Error we do this:
    # with self.assertRaises(ZeroDivisionError):
    #     SimpleCalculator().divide(10,0)
    # or assert.assertraises(ZeroDivisionError,SimpleCalculator().divide, 10,0)