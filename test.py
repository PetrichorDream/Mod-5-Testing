import unittest

from my_sum import sum

from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()

"""

Test Results Summary:
- Ran 2 unit tests using the unittest framework
- test_list_int passed producing 6 matching the predicted result
- test_list_fraction failed resulting in Fraction(9, 10) (0.9) instead of expected value of 1 triggering an assertion error

"""
