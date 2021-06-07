#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


def count_words(path_to_file):
    """
    Zählt alle Wörter in einem File, welches mit Pfad der Funktion übergeben wird.
    Zeichen die mit einem Apostroph verbunden sind, sind ein Wort. Beispiel <don't>. Namen wie Hans-Peter sind
    ebenfalls ein Wort.

    Entfernt alle nicht erlaubten Zeichen aus dem Text und ersetzt diese Zeichen durch ein Leerzeichen. Weitere erlaubte
    Zeichen zwischen die beiden äußeren eckigen Klammern setzen.
    """
    with open(path_to_file) as file:
        text = file.read()
    valid = re.sub(r"[^A-Za-z'-]+", ' ', text)
    return len(valid.split())


def count_character(path_to_file):
    """
    Zählt alle Zeichen in einem File, welches mit Pfad der Funktion übergeben wird.

    Entfernt alle nicht erlaubten Zeichen aus dem Text und baut einen zusammenhängenden String. Leerzeichen gehören
    auch nicht zu den erlaubten Zeichen. Weitere erlaubte Zeichen zwischen die beiden äußeren eckigen Klammern setzen.
    """
    with open(path_to_file) as file:
        text = file.read()
    valid = re.sub(r"[^A-Za-z!\"#$%&'()*+,-./0-9:;<=>?@\[\\\]\^_`{|}~]+", '', text)
    return len(valid)


def count_lines(path_to_file):
    """
    Zählt alle Zeilen in einem File, welches mit Pfad der Funktion übergeben wird.

    Andere Lösungen:
    https://www.codespeedy.com/count-the-number-of-lines-in-a-text-file-in-python/
    Getestet mit: https://pythonspot.com/python-profiling/
    Meine Variante mit cProfile: 2686 function calls (2647 primitive calls) in 0.009 seconds
    1st Variante auf pythonspot: 2688 function calls (2649 primitive calls) in 0.011 seconds
    2nd Variante auf pythonspot: 2703 function calls (2664 primitive calls) in 0.009 seconds
    """
    lines = 0
    with open(path_to_file) as file:
        for line in file:
            lines += 1
    return lines


def count_words_from_line(path_to_file, specific_line):
    """
    Zählt alle Wörter in einem File in einer spezifischen Zeile, welches mit Pfad der Funktion und der Zeile
    übergeben wird. Zeichen die mit einem Apostroph verbunden sind, sind ein Wort. Beispiel <don't>. Namen
    wie Hans-Peter sind ebenfalls ein Wort.

    Entfernt alle nicht erlaubten Zeichen aus dem Text und ersetzt diese Zeichen durch ein Leerzeichen. Weitere erlaubte
    Zeichen zwischen die beiden äußeren eckigen Klammern setzen.
    """
    if specific_line < 1: return 0
    if specific_line > count_lines(path_to_file): return 0
    with open(path_to_file) as file:
        for line_number, line in enumerate(file):
            if line_number+1 == specific_line:
                valid_char = re.sub(r"[^A-Za-z'-]+", ' ', line)
                return len(valid_char.split())
    return 0


def count_quotes(path_to_file):
    with open(path_to_file) as file:
        text = file.read()
    valid_char = re.sub(r"[^A-Za-z\"\n]+", '', text)
    valid = valid_char.split("\n")
    count_quote = 0
    start_quote_det = False
    end_quote_det = False
    for element in valid:
        #print(element)
        if element.startswith("\""):
            if not start_quote_det:
                start_quote_det = True
            else:
                start_quote_det = False
                end_quote_det = False
        elif element.endswith("\""):
            if not end_quote_det:
                end_quote_det = True
                print("Zitatende")
                #print(str(start_quote_det) + " and " + str(end_quote_det))
            else:
                start_quote_det = False
                end_quote_det = False
        elif start_quote_det and end_quote_det:
            print("lala")
            print(element.startswith("\""))
            print(element.endswith("\""))
            if len(element) > 0 and not element.startswith("\"") and not element.endswith("\""):
                count_quote += 1
                start_quote_det = False
                end_quote_det = False
                print(f'Test: {element}')
            elif element.startswith("\""):
                start_quote_det = True
            else:
                start_quote_det = True
            end_quote_det = False
    return count_quote


def count_sentences(path_to_file):
    """
    Zählt alle Sätze in einem File, welches mit Pfad der Funktion übergeben wird.
    Sätze werden dadurch definiert, dass diese mit einem Satzzeichen <.>, <!> oder <?> enden.
    Spannungsbögen <...>, werden gefilter und zählt zu einem Satz dazu.
    """
    with open(path_to_file) as file:
        text = file.read()
    valid_char = re.sub(r"[^A-Za-z.!?]+", '', text)
    no_suspense = re.sub(r"\.\.\.", "", valid_char)
    sentences_list = re.split("\.|\!|\?", no_suspense)
    return len([sentences for sentences in sentences_list if len(sentences) > 0])


def count_character_all(path_to_file):
    """
    Zählt alle Zeichen inklusive der Leerzeichen in einem File, welches mit Pfad der Funktion übergeben wird.

    Entfernt alle nicht erlaubten Zeichen aus dem Text und baut einen zusammenhängenden String. Weitere erlaubte
    Zeichen zwischen die beiden äußeren eckigen Klammern setzen.

    Das Problem hier war, wenn die Zeichenfolge:
    > Sullivan id s   s  s
    >
    > d
    >
    Zählt man über \s auch die LF mit. Diese werden am Ende noch einmal vom Ergebnis abgezogen.
    """
    with open(path_to_file) as file:
        text = file.read()
    valid_char = re.sub(r"[^A-Za-z!\"#$%&'()*+,-./0-9:;<=>?@\[\\\]\^_`{|}~[\s]]+", '', text)
    lf_count = re.findall(r"[\n]", valid_char)
    return len(valid_char)-len(lf_count)


def main():
    pass


if __name__ == "__main__":
    main()
