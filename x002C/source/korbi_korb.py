from pathlib import Path
import re


def count_words(file_path) -> int:
    """
    IDEA:
    Step 1. remove any non-word character but not "space" or "line feed" or "carriage return"
    Step 2. letter, digit or underscore separated with space => represents word =>
    "\w" machtes in Regex all letter, digit or underscore. "+" is the extension till next space
    """
    counted_word = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            replaced = re.sub("[\W](?<![ \n\r])", "", text)  # Step 1
            x = re.findall("\w+", replaced)  # Step 2
            counted_word = len(x)
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted words: " + str(counted_word))

    return counted_word


def count_character(file_path) -> int:
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


def count_words_from_line(file_path, line) -> int:
    """
    IDEA:
    Step 1. Check if provided "line" is not zero and "line" is not above max lines of file
    Step 2. remove any non-word character but not "space" or "line feed" or "carriage return" from line
    Step 3. letter, digit or underscore separated with space => represents word =>
    "\w" machtes in Regex all letter, digit or underscore. "+" is the extension till next space
    """
    counted_words_in_line = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            lines = current_file.readlines()
            if line != 0 and line <= len(lines):  # Step 1
                replaced = re.sub("[\W](?<![ \n\r])", "", lines[line - 1])  # Step 2
                x = re.findall("\w+", replaced)  # Step 3
                counted_words_in_line = len(x)
            else:
                print("line out of range")
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted words: " + str(counted_words_in_line) + " in line " + str(line))

    return counted_words_in_line


def count_sentences(file_path) -> int:
    """
    IDEA:
    In german language there are three "satzschlusszeichen".
    dot (.) Question mark (?) exclamation mark (!)
    Count every of these occurrences followed by a space.
    Example:
    " My name is korbi and sometimes. I like python !? " => 2 sentence
    " My name is korbi and sometimes... I have good ideas. " => 1 sentence
    " hee!lo my name is korbi" => 1 sentence
    Step1. Remove multiple ussage of Question mark (?) exclamation mark (!) to avoid !? are two sentences
    Step2: Find all dot (.) Question mark (?) exclamation mark (!) but allow "..."
    """
    counted_sentences = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            replaced = re.sub("[\?\!]+(?=[\?\!])", "", text)  # Step 1
            x = re.findall("(?<!\.)[.?!](?!\.)", replaced)  # Step 2
            counted_sentences = len(x)
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted sentences: " + str(counted_sentences))

    return counted_sentences


def count_quotes(file_path) -> int:
    """
    Very hard .... even words is not able to detect quotes reliable ...
    IDEA:
    Step1. Count all "
    Step2: Divide by 2 without rest
    """
    counted_quotes = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            x = re.findall('["]', text)  # Step 2
            counted_quotes = len(x) // 2
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted quotes: " + str(counted_quotes))

    return counted_quotes


def count_character_all(file_path) -> int:
    """
    IDEA:
    Step 1. Count everything in ASCII TABLE from 32 (Space) to 126 (~)
    """
    counted_character_all = 0
    try:
        with open(Path(file_path), "r", encoding="utf8") as current_file:
            text = current_file.read()
            x = re.findall("[ -~]", text)  # Step 1
            counted_character_all = len(x)
    except IOError as e:
        print("I/O error" + str((e.errno, e.strerror)))
    else:
        print("Counted counted characters: " + str(counted_character_all))

    return counted_character_all
