#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filter_chars_words = [".", "!", "?", "\"", ",", "'", "-", "â€•", "\n"]
filter_chars_words = ["â", "•", "\n"]


def count_words(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    for element in filter_chars_words:
        text = text.replace(element, " ")
    words = text.split()
    return len(words)


def count_character(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    for element in filter_chars_words:
        text = text.replace(element, "")
    text = text.replace(" ", "")
    return len(text)


def count_lines(path_to_file):
    lines = 0
    with open(path_to_file) as file:
        for line in file:
            lines += 1
    return lines


def main():
    pass


if __name__ == "__main__":
    main()
