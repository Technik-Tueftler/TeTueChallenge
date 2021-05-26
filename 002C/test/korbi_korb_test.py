import unittest
from ..source.korbi_korb import *


class RankPlayerTestCase(unittest.TestCase):

    def test_tetü_test_count_words(self):
        self.assertEqual(251, count_words('002C/test/testfile.txt'))

    def test_tetü_test_count_chars(self):
        self.assertEqual(1043, count_char('002C/test/testfile.txt'))

    def test_tetü_test_count_lines(self):
        self.assertEqual(15, count_lines('002C/test/testfile.txt'))

    def test_tetü_test_count_words_in_line(self):
        self.assertEqual(19, count_words_from_line('002C/test/testfile.txt', 1))

    def test_tetü_test_count_words_in_empty_line(self):
        self.assertEqual(0, count_words_from_line('002C/test/testfile.txt', 4))


if __name__ == '__main__':
    unittest.main()
