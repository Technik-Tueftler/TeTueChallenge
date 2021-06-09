import sys
import os
import unittest

#Do akward stuff to import fingerprint_invalid
directory = os.path.dirname( sys.argv[0])
path = os.path.join( directory, '..\\source')
sys.path.insert( 0, path)
from fingerprint_invalid import *

# from  ..source.fingerprint_invalid import * # That seems to only work in pycharm.
# I dont like IDE dependent features. 

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
def get_path_to_testfile(): # because I am to lazy to type that more than once
    p = os.path.join( os.path.dirname(sys.argv[0]), "..\\test\\testfile.txt")
    return p

def main():
    unittest.main()

if __name__ == "__main__":
    main()