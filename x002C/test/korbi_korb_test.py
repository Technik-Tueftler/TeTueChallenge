import unittest

"""
Kompletter import ohne package: from x002C.source.technik_tueftler import count_lines as count_lines_tetue
"""
from x002C.source import count_lines_korbi, count_words_korbi, count_character_korbi
from x002C.source import count_words_from_line_korbi, count_sentences_korbi, count_quotes_korbi, count_character_all_korbi
import pathlib

# print(pathlib.Path.cwd().parent.joinpath("testfile.txt")) Wenn das File eine Ebene höher liegt
PATH_TO_TEST_FILE = pathlib.Path(r'C:\Users\Korbi\PycharmProjects\TeTueChallenge\x002C\test\testfile.txt')
print(PATH_TO_TEST_FILE)

class CountTetuesStuffTestCase(unittest.TestCase):

    def test_tetü_test_count_words(self):
        self.assertEqual(240, count_words_korbi(PATH_TO_TEST_FILE))

    def test_tetü_test_count_character(self):
        self.assertEqual(1042, count_character_korbi(PATH_TO_TEST_FILE))

    def test_tetü_test_count_lines(self):
        self.assertEqual(16, count_lines_korbi(PATH_TO_TEST_FILE))

    def test_tetü_test_count_words_in_line(self):
        self.assertEqual(19, count_words_from_line_korbi(PATH_TO_TEST_FILE, 1))

    def test_tetü_test_count_words_in_empty_line(self):
        self.assertEqual(0, count_words_from_line_korbi(PATH_TO_TEST_FILE, 4))

    def test_tetü_test_count_sentences(self):
        self.assertEqual(16, count_sentences_korbi(PATH_TO_TEST_FILE))

    def test_tetü_test_count_quotes(self):
        self.assertEqual(1, count_quotes_korbi(PATH_TO_TEST_FILE))

    def test_tetü_test_character_all(self):
        self.assertEqual(1271, count_character_all_korbi(PATH_TO_TEST_FILE))


if __name__ == '__main__':
    unittest.main()
