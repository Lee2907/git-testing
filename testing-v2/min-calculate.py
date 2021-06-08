import unittest
from main import MyMiniCalculator


class TestMiniCalculator(unittest.TestCase):
    def test_add(self):
        add_object = MyMiniCalculator()
        self.assertEqual(add_object.add(1, 1), 2), "Incorrect addition. Answer should be two"
