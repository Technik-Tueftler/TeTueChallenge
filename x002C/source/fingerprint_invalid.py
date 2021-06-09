import os
import sys

def count_words(path_to_file): 
    allLinesInOne = ''.join(readLinesFromFile(path_to_file))
    return len(allLinesInOne.split())

def count_character(path_to_file):
    allLinesInOneWithOutNewLinesandSpaces = ''.join(readLinesFromFile(path_to_file)).replace('\n', '').replace('\r', '').replace(' ','')
    return len(allLinesInOneWithOutNewLinesandSpaces)

def count_lines(path_to_file):
    return(len(readLinesFromFile(path_to_file)))

# Zusatzaufgaben
def count_words_from_line(path_to_file, linennumber):
    return len(readLinesFromFile(path_to_file)[linennumber].split())

def count_sentences(path_to_file): 
    allLinesInOneWithOutNewLinesandSpaces = ''.join(readLinesFromFile(path_to_file)).replace('\n', '').replace('\r', '').replace(' ','')
    CharArray = [char for char in allLinesInOneWithOutNewLinesandSpaces]
    numberOfSentences = 0
    for i in range(len(CharArray)): # loop over all chars and check for . ? ! for Detecting a sentence. Just single points are detected as a sentence
        c = CharArray[i]
        if c == '.':
            if(i == 0): # . is first char in whole text
                if (CharArray[i+1] != '.'):
                    numberOfSentences = numberOfSentences + 1
                    continue
            if(i == (len(CharArray)-1)):# . is last char in whole text
                if (CharArray[i-1] != '.'):
                    numberOfSentences = numberOfSentences + 1
                    continue
            if (CharArray[i-1] != '.') and (CharArray[i+1] != '.'):
                    numberOfSentences = numberOfSentences + 1
                    continue
        if (c == '!') or (c == '?'): # Other signs
                numberOfSentences = numberOfSentences + 1
    return numberOfSentences

def count_quotes(path_to_file):
    allLinesInOneWithOutNewLinesandSpaces = ''.join(readLinesFromFile(path_to_file)).replace('\n', '').replace('\r', '').replace(' ','')
    return int(allLinesInOneWithOutNewLinesandSpaces.count('"')/2)

def count_character_all(path_to_file):
    allLinesInOneWithOutNewLines = ''.join(readLinesFromFile(path_to_file)).replace('\n', '').replace('\r', '')
    return len(allLinesInOneWithOutNewLines)

def readLinesFromFile(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.readlines()