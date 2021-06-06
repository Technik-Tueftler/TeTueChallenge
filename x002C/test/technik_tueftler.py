#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Kompletter import ohne package: from x002C.source.technik_tueftler import count_lines as count_lines_tetue
"""
from x002C.source import count_lines_tetue, count_words_tetue, count_character_tetue
import pathlib

# print(pathlib.Path.cwd().parent.joinpath("testfile.txt")) Wenn das File eine Ebene höher liegt
PATH_TO_TEST_FILE = pathlib.Path.cwd().joinpath("testfile.txt")


def main():
    print(f'Anzahl der Wörter: {count_words_tetue(PATH_TO_TEST_FILE)}')
    print(f'Anzahl der Zeichen: {count_character_tetue(PATH_TO_TEST_FILE)}')
    print(f'Anzahl der Zeilen: {count_lines_tetue(PATH_TO_TEST_FILE)}')


if __name__ == "__main__":
    main()
