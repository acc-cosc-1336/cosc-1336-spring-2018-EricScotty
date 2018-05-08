import unittest
from src.assignments.assignment1 import add_numbers
from src.assignments.assignment1 import multiply_numbers
from src.assignments.assignment1 import square_number

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self):
        self.assertEqual(2, add_numbers(1, 1))

    def test_add_numbers_25(self):
        self.assertEqual(50, add_numbers(25, 25))

    def test_add_numbers_50(self):
        self.assertEqual(100, add_numbers(50, 50))

    def test_multiply_numbers_product_1(self):
        self.assertEqual(1, multiply_numbers(1,1))

    def test_multiply_numbers_product_20(self):
        self.assertEqual(20, multiply_numbers(5,4))

    def test_multiply_numbers_product_45(self):
        self.assertEqual(45, multiply_numbers(5,9))

    def test_square_number_1(self):
        self.assertEqual(1, square_number(1))

    def test_square_number_5(self):
        self.assertEqual(25, square_number(5))

    def test_square_number_10(self):
        self.assertEqual(100, square_number(10))
