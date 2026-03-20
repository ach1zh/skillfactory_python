# tests/test_utils.py
import unittest
from src.utils import calculate_interest, compound_interest

class TestUtils(unittest.TestCase):
    def test_calculate_interest(self):
        self.assertEqual(calculate_interest(1000, 5, 1), 50)

    def test_compound_interest(self):
        self.assertAlmostEqual(compound_interest(1000, 0.05, 12, 1), 51.161897881733754)

if __name__ == '__main__':
    unittest.main()