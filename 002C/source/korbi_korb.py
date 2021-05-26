from pathlib import Path
import re


def count_words(file_path) -> int:
    """
    IDEA:
    Step 1. letter, digit or underscore separated with space => represents word =>
    "\w" machtes in Regex all letter, digit or underscore. "+" is the extension till next space
    """
    counted_word = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            x = re.findall("\w+", text)  # Step 1
            counted_word = len(x)
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted words: " + str(counted_word))

    return counted_word


def count_char(file_path) -> int:
    """
    IDEA:
    Step 1. Remove all spaces
    Step 2. Count everything in ASCII TABLE from 33 (!) to 126 (~)
    """
    counted_char = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            replaced = re.sub("\s", "", text)  # Step 1
            x = re.findall("[!-~]", replaced)  # Step 2
            counted_char = len(x)
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted chars: " + str(counted_char))

    return counted_char


def count_lines(file_path) -> int:
    """
    Expectation is that a line ends with CRLF
    CR \r Carriage Return set the cursor to next line
    LR \n Newline create a "new line"
    \r without \n is not a new line in from my point of view
    Therefore count all \n to get all "new line" expressions
    IDEA:
    Step 1. Count \n
    Step 2. Add +1 to get the get also the last line which must not ends with CRLF
    """
    counted_lines = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            x = re.findall("\n", text)  # Step 1
            counted_lines = len(x) + 1  # Step 2
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted lines: " + str(counted_lines))

    return counted_lines


def count_words_from_line(file_path, row) -> int:
    """
    Expectation is that a line ends with CRLF
    CR \r Carriage Return set the cursor to next line
    LR \n Newline create a "new line"
    \r without \n is not a new line in from my point of view
    Therefore count all \n to get all "new line" expressions
    IDEA:
    Step 1. Count \n
    Step 2. Add +1 to get the get also the last line which must not ends with CRLF
    """
    counted_words_in_line = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            lines = current_file.readlines()
            if row != 0 and row <= len(lines) :
                x = re.findall("\w+", lines[row-1])  # Step 1
                counted_words_in_line = len(x)
            else:
                print("line out of range")
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted words: " + str(counted_words_in_line) + " in line " + str(row))

    return counted_words_in_line
