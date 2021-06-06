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


def main():
    pass


if __name__ == "__main__":
    main()
