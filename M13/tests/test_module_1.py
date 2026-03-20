import unittest
from M13.src.module_1 import add

class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1, 2), 3)

    def test_2(self):
        self.assertEqual(add(-1, 1), 0)

    def test_3(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_4(self):
        self.assertEqual(add(0, 0), 1)

if __name__ == '__main__':
    unittest.main()
