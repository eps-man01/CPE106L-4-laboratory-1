import unittest
from src.main import multiply


class TestMultiplierLogic(unittest.TestCase):
    
    def test_multiply_by_two(self):
        self.assertEqual(multiply(4, 1), 8)
        
    def test_multiply_by_three(self):
        self.assertEqual(multiply(7, 2), 21)
        
    def test_custom_multiplier(self):
        self.assertEqual(multiply(5, 3, 4), 20)


if __name__ == '__main__':
    unittest.main()
