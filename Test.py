import unittest

from Add import add
from Factorial import factorial

class TestSum(unittest.TestCase):
    def test_list_int(self):
        # Test case to add two numbers
        a = 15
        b = 32
        sum = add(a, b)
        
        # Test case to find factorial
        c = 4
        fact = factorial(c)
        
        self.assertEqual(sum, 47)
        self.assertEqual(fact, 24)

if __name__ == '__main__':
    unittest.main()
