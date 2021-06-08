import unittest
from ..source.korbi_korb import *


class CountTetuesStuffTestCase(unittest.TestCase):

    def test_tetü_test_count_words(self):
        self.assertEqual(240, count_words('002C/test/testfile.txt'))

    def test_tetü_test_count_chars(self):
        self.assertEqual(1043, count_char('002C/test/testfile.txt'))

    def test_tetü_test_count_lines(self):
        self.assertEqual(15, count_lines('002C/test/testfile.txt'))

    def test_tetü_test_count_words_in_line(self):
        self.assertEqual(19, count_words_from_line('002C/test/testfile.txt', 1))

    def test_tetü_test_count_words_in_empty_line(self):
        self.assertEqual(0, count_words_from_line('002C/test/testfile.txt', 4))

    def test_tetü_test_count_sentences(self):
        self.assertEqual(16, count_sentences('002C/test/testfile.txt'))

    def test_tetü_test_count_quotes(self):
        self.assertEqual(1, count_quotes('002C/test/testfile.txt'))

    def test_tetü_test_character_all(self):
        self.assertEqual(1272, count_character_all('002C/test/testfile.txt'))


if __name__ == '__main__':
    unittest.main()
