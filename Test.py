import unittest

from Add import add
from Factorial import factorial

class TestSum(unittest.TestCase):
    def test_list_int(self):
        # Test case to add two numbers
        a = 15
        b = 10
        sum = add(a, b)
        
        # Test case to find factorial
        c = 6
        fact = factorial(c)
        
        self.assertEqual(sum, 25)
        self.assertEqual(fact, 720)

if __name__ == '__main__':
    unittest.main()
