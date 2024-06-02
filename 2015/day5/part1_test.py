import unittest
from part1 import is_nice

class TestNaughtyOrNice(unittest.TestCase):
    def test_forbidden_pair(self):
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))

    def test_simple_nice(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))

    def test_overlap_nice(self):
        self.assertTrue(is_nice("aaa"))

    def test_no_double_letter(self):
        self.assertFalse(is_nice("jchzalrnumimnmhp"))

    def test_not_enough_vowels(self):
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))

if __name__ == '__main__':
    unittest.main()
