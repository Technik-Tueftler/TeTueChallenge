# DE
Die Aufgabe kann auch in jeder anderen Sprache umgesetzt werden, wenn die Anforderungen erfüllt werden von der 
Struktur her und keine extra Tools und Programme gebraucht werden.
## Anforderungen (Weitere Regeln)
1. Die Funktionen müssen unter Python 3.10 laufen.
2. Maximal zwei Dateien erlaubt. Funktionsfile und ein Testfile in den jeweiligen Ordnern.
3. Das Testfile (falls vorhanden) muss eigenständig ausführbar sein.
4. Das File mit den Funktionen muss unter *source* abgelegt werden mit dem Dokumentenname *twitchname*.py
   in Kleinbuchstaben. Weitere Informationen, Ideen und Anmerkungen jeweils im Modul mit
   Kommentaren einfügen und dokumentieren.
5. Ein Testfile unter *test* mit dem Namen *twitchname*_test.py in Kleinbuchstaben, falls benötigt.
6. Der letzte Commit muss bis 07.12.2021 19:00 Uhr gepushed sein.
7. Bitte die fertig entwickelten Funktionen, welche ihr freigeben wollt, in die source/__init__.py eintragen.

## Aufgabe
Die Aufgabe 2 soll erweitert werden. Es sollen die verschiedene Elemente einer Website analysiert und ausgewertet werden. Folgende Funktionen sollen implementiert werden:
1. Zählen aller Wörter in einem dictionary.
```python
def collect_words_from_website(collect_words: dict, url: str | int) -> None:
    """
    Collect all the words from a website in a transferred dictionary. All letters are converted into lowercase letters.
    Structure of the dictionary: word_list[<word: str>] = <number: int>

            Parameters:
                    collect_words (dict): Dictionary to count all words
                    url (str): Full url to website

            Returns:
                    None
    """
    pass
```
2. Sammle alle absoluten Links auf einer Website in einer Liste.
```python
def collect_links_from_website(collect_links: list[str], url: str) -> None:
    """
    Collect all the absolute links from a website in a transferred list.

            Parameters:
                    collect_links (list): List to collect all links as string.
                    url (str): Full url to website

            Returns:
                    None
    """
    pass
```

3. Sammle alle Bildnamen auf einer Website in einer Liste.
```python
def collect_picture_names_from_website(collect_picture_names: list[str], url: str) -> None:
    """
    Collect all the picture names with file format and without path from a website in a transferred list.

            Parameters:
                    collect_picture_names (list): List to collect all picture names as string.
                    url (str): Full url to website

            Returns:
                    None
    """
    pass
```

## Fehlerbehandlung
Da es rein um die Aufgabe geht und den Lösungsweg, vernachlässigen wir die Fehlerbehandlung. 
Es wird immer davon ausgegangen, dass die übergebenen Parameter im korrekten Wertebereich sind und der übergebene
Pfad existiert.

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch. Grundlegend stelle ich mir die Abstufungen aber wie folgt vor:
1. Aufgabe erfüllt/nicht erfüllt
2. Anforderungen erfüllt und umgesetzt

## Ergebnisse