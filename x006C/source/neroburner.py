#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import hashlib
import os
import requests
import re

def get_html(url : str) -> str:
    """get the html of a url only once. Cache the contents of the retrieved url
    in a file with the hashed url as filename. Use the cached content instead
    of requesting the page again and again"""
    sha = hashlib.md5(url.encode("utf-8")).hexdigest()
    filename = sha + ".html"
    if os.path.exists(filename):
        with open(filename) as f:
            html = f.read()
    else:
        r = requests.get(url)
        html = r.content.decode("utf-8")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
    return html

# 1. Zählen aller Wörter in einem dictionary.
def collect_words_from_website(collect_words: dict, url: str) -> None:
    """
    Collect all the words from a website in a transferred dictionary. All letters are converted into lowercase letters.
    Structure of the dictionary: word_list[<word: str>] = <number: int>

            Parameters:
                    collect_words (dict): Dictionary to count all words
                    url (str): Full url to website

            Returns:
                    None
    """
    # assume words are only inside <p>...</p> paragraps
    html = get_html(url)
    word_list = dict()
    matches = re.findall('<p[^>]*>(.*)</p>', html)
    for paragraph in matches:
        # get rid of html tags in the extracted paragraph
        cleaned_paragraph = re.sub('<[/]?[^>]*>', '', paragraph)
        lower_paragraph = cleaned_paragraph.lower()
        # split and count words
        words = lower_paragraph.split()
        for w in words:
            if w in word_list:
                word_list[w] += 1
            else:
                word_list[w] = 1
    # return the most counted words first
    for key, val in sorted(word_list.items(), key=lambda x:x[1], reverse=True):
        collect_words[key] = val
    pass

# 2. Sammle alle absoluten Links auf einer Website in einer Liste.
def collect_links_from_website(collect_links: list[str], url: str) -> None:
    """
    Collect all the absolute links from a website in a transferred list.

            Parameters:
                    collect_links (list): List to collect all links as string.
                    url (str): Full url to website

            Returns:
                    None
    """
    html = get_html(url)
    matches = re.findall('<a[ \t]+href="(http[s]?://[^"]+?)"', html)
    urls = [m.strip() for m in matches]
    collect_links += urls
    pass

# 3. Sammle alle Bildnamen auf einer Website in einer Liste.
def collect_picture_names_from_website(collect_picture_names: list[str], url: str) -> None:
    """
    Collect all the picture names with file format and without path from a website in a transferred list.

            Parameters:
                    collect_picture_names (list): List to collect all picture names as string.
                    url (str): Full url to website

            Returns:
                    None
    """
    html = get_html(url)
    matches = re.findall('(?:<img[ \t].*)src="([^"]+?)"', html)
    filenames = [os.path.basename(m) for m in matches]
    collect_picture_names += filenames
    pass

def main():
    parser = argparse.ArgumentParser(description="NeroBurners solution to TeTue Challenge 6")
    parser.add_argument("url", type=str, help="Website URL to parse",
        nargs="?", # passing url is optional
        default="https://www.w3schools.com/default.asp")
    args = parser.parse_args()
    # return variables
    collect_words = dict()
    collect_links = []
    collect_picture_names = []
    # call the implemented challenges
    collect_words_from_website(collect_words, args.url)
    collect_links_from_website(collect_links, args.url)
    collect_picture_names_from_website(collect_picture_names, args.url)
    # print the found results
    print("words: ", collect_words, "\n")
    print("links: ", collect_links, "\n")
    print("pics:  ", collect_picture_names, "\n")

if __name__ == "__main__":
    main()
