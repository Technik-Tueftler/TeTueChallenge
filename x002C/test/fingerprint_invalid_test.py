import sys
import pathlib
import unittest

sys.path.append(str(pathlib.Path.cwd().parent.parent))
from x002C.source.fingerprint_invalid import *


# Definition of test cases.
class TestTetuesChallangeStuff(unittest.TestCase):

    def test_count_words_from_line(self):
        result = count_words_from_line(get_path_to_testfile(), 2)
        self.assertEqual(result, 12)
        print("File contains: " + str(result) + " words in line 2")

    def test_count_lines(self):
        result = count_lines(get_path_to_testfile())
        self.assertEqual(result, 15)
        print("File contains: " + str(result) + " lines")

    def test_count_words(self):
        result = count_words(get_path_to_testfile())
        self.assertEqual(result, 242)
        print("File contains: " + str(result) + " words")

    def test_count_character(self):
        result = count_character(get_path_to_testfile())
        self.assertEqual(result, 1045)
        print("File contains: " + str(result) + " charachters")

    def test_count_sentences(self):
        result = count_sentences(get_path_to_testfile())
        self.assertEqual(result, 16)
        print("File contains: " + str(result) + " sentences")

    def test_count_quotes(self):
        result = count_quotes(get_path_to_testfile())
        self.assertEqual(result, 1)
        print("File contains: " + str(result) + " quotes")


# Support Functions
def get_path_to_testfile():
    return pathlib.Path.cwd().joinpath("testfile.txt")


def main():
    unittest.main()


if __name__ == "__main__":
    main()