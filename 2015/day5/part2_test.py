import unittest
from part2 import is_nice, has_repeated_letter_separated_by_one, has_non_overlapping_repeated_pair

class TestIsNice(unittest.TestCase):
    def test_repeat_pair_without_repeat_char(self):
        self.assertFalse(is_nice("rcxstgmygtbstg"))

    def test_repeat_char_without_repeat_pair(self):
        self.assertFalse(is_nice("ieodomkazucvgmuy"))

    def test_repeat_pair_that_overlaps(self):
        self.assertFalse(is_nice("abaxxx"))

    def test_repeating_pair_and_one_letter_separation(self):
        self.assertTrue(is_nice("xxyxx"))

class TestHasRepeatedLetterSeparatedByOne(unittest.TestCase):
    def test_too_short(self):
        self.assertFalse(has_repeated_letter_separated_by_one("aa"))

    def test_three_char_word(self):
        self.assertTrue(has_repeated_letter_separated_by_one("aba"))

    def test_long_word(self):
        self.assertTrue(has_repeated_letter_separated_by_one("ajsweralrwexyxjewrtkj"))

class TestHasNonOverlappingRepeatedPair(unittest.TestCase):
    def test_no_pairs(self):
        self.assertFalse(has_non_overlapping_repeated_pair("abcdefgh"))

    def test_overlapping_pair(self):
        self.assertFalse(has_non_overlapping_repeated_pair("aaa"))

    def test_non_overlapping_repeated_pair(self):
        self.assertTrue(has_non_overlapping_repeated_pair("abab"))

    def test_non_overlapping_repeated_pair_with_separation(self):
        self.assertTrue(has_non_overlapping_repeated_pair("abkjsdfkjdfabmm"))


if __name__ == '__main__':
    unittest.main()
