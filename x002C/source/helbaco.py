import re
import sys


# ich mich an der implementation von wc orientiert, 
# weshalb in der regel keine zeichen ersetzt werden (doppelnamen etc)
# https://man7.org/linux/man-pages/man1/wc.1.html

testfile = '../test/testfile.txt'


def count_words(filepath):
    try:
        with open(filepath, mode='rt') as file:
            return len(file.read().split())
    except (IOError, OSError) as e:
        print_n_out(e)


def count_character(filepath):
    try:
        with open(filepath, mode='rt') as file:
            return len(file.read().replace(' ', ''))
    except (IOError, OSError) as e:
        print_n_out(e)


def count_lines(filepath):
    try:
        with open(filepath, mode='rt') as file:
            return sum(1 for line in file)
            # return sum(1 for _ in file) # Wenn Variable nicht benutzt wird, kann man diese durch eine <_> ersetzen
            # return sum(1 for count, line in enumerate(file) if count % 2)
    except (IOError, OSError) as e:
        print_n_out(e)


def count_words_from_line(filepath, targetline):
    if targetline > count_lines(filepath) or targetline < 1:
        print_n_out('line not found')
    try:
        with open(filepath, mode='rt') as file:
            return len(file.readlines()[targetline-1].split())
    except (IOError, OSError) as e:
        print_n_out(e)


def count_sentences(filepath):
    try:
        with open(filepath, mode='rt') as file:
            sentences = re.split(r'[!?]+|(?<!\.)\.(?!\.)', file.read().replace('\n',''))          
    except (IOError, OSError) as e:
        print_n_out(e)

    sentences = sentences[:-1]
    sentence_count = len(sentences)
    return sentence_count


def count_quotes(filepath):
    # count texts between "
    try:
        with open(filepath, mode='rt') as file:
            return len(re.findall(r'"(.*?)"', file.read().replace("\n", "")))
    except (IOError, OSError) as e:
        print_n_out(e)


def count_character_all(filepath):
    try:
        with open(filepath, mode='rt') as file:
            return len(file.read())
    except (IOError, OSError) as e:
        print_n_out(e)


def print_n_out(error):
    print(error)
    sys.exit()


def main():
    print(f'lines: {count_lines(testfile)}')
    print(f'words: {count_words(testfile)}')
    print(f'chars: {count_character(testfile)}')
    print(f'words in line(x): {count_words_from_line(testfile, 14)}')
    print(f'sentences: {count_sentences(testfile)}')
    print(f'quotes: {count_quotes(testfile)}')
    print(f'chars (all): {count_character_all(testfile)}')


if __name__ == "__main__":
    main()
