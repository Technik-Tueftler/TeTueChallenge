# DE
Die Aufgabe kann auch in jeder anderen Sprache umgesetzt werden, wenn die Anforderungen erfüllt werden von der 
Struktur her und keine extra Tools und Programme gebraucht werden.
## Anforderungen (Weitere Regeln)
1. Die Funktionen müssen unter Python 3.8 laufen.
2. Maximal zwei Dateien erlaubt. Funktionsfile und ein Testfile in den jeweiligen Ordnern.
3. Das Testfile (falls vorhanden) muss eigenständig ausführbar sein.
4. Das File mit den Funktionen muss unter *source* abgelegt werden mit dem Dokumentenname *twitchname*.py
   in Kleinbuchstaben. Weitere Informationen, Ideen und Anmerkungen jeweils im Modul mit
   Kommentaren einfügen und dokumentieren.
5. Ein Testfile unter *test* mit dem Namen *twitchname*_test.py in Kleinbuchstaben, falls benötigt.
6. Der letzte Commit muss bis 03.11.2021 19:00 Uhr gepushed sein.
7. Bitte die fertig entwickelten Funktionen, welche ihr freigeben wollt, in die source/__init__.py eintragen.

## Aufgabe
Die Aufgabe ist eine Erweiterung aus der Challenge 3 und soll unser Spiel *Schiffeversenken* erweitern. Schreibt eine Funktion, die ein Schiff, zufällig, in das Spielfeld einfügt. Die nachfolgenden Regeln sollten erfüllt sein:
1. Die Felder müssen frei sein und dürfen nicht durch ein anderes Schiff belegt sein.
2. Legale Schiffspositionen sind nur waagerecht und senkrecht. Also keine Diagonalen.

Die Funktion sollte so aufgerufen werden:
```python
def set_new_battleship(battlefield: list, ship_size: int, ship_sign: str) -> None:
    pass
```
**battlefield:** ist die zweidimensionale Liste. Diese könnt ihr so generieren:
```python
battlefield = [[0] * 10 for i in range(10)]
```

`ship_size:` Ist die Schiffslänge. Die sollte nicht kleiner sein als 3 und nicht größer als 5.  
`ship_sign:` Ist das Zeichen im Spielfeld für dieses Schiff.  


## Fehlerbehandlung
Da es rein um die Aufgabe geht und den Lösungsweg, vernachlässigen wir die Fehlerbehandlung. 
Es wird immer davon ausgegangen, dass die übergebenen Parameter im korrekten Wertebereich sind und der übergebene
Pfad existiert.

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch. Grundlegend stelle ich mir die Abstufungen aber wie folgt vor:
1. Aufgabe erfüllt/nicht erfüllt
2. Anforderungen erfüllt und umgesetzt

## Ergebnisse
Hier werden alle Ergebnisse der einzelnen Teilnehmer aufgeschrieben.
### Technik Tüftler
#### Zusammenfassung
`technik_tueftler_11` 491 Aufrufe  
`technik_tueftler_12` 479 Aufrufe  
`technik_tueftler_13` 153 Aufrufe  
`technik_tueftler_14` 53 Aufrufe  
`technik_tueftler_21` 481 Aufrufe  
`technik_tueftler_22` 485 Aufrufe  
#### Einzel
`technik_tueftler_11:`  Erste Version. Ohne Optimierungen
Durchschnitt (von 20 Ausführungen) 491 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 250
- int: 102
- len: 13
- combine_numbers: 100

`technik_tueftler_12:`  Aus dem battle_field wurde eine eindimensionale Liste. 
Durchschnitt (von 20 Ausführungen) 479 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 240
- int: 102
- len: 2
- combine_numbers: 100

`technik_tueftler_13:`  random.shuffle entfernt für die Liste entfernt
Durchschnitt (von 20 Ausführungen) 153 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 13
- int: ca. 7
- len: 14
- combine_numbers: 100

`technik_tueftler_14:`  entfernen des Funktionsaufrufs aus der list comprehension 
Durchschnitt (von 20 Ausführungen) 53 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 13
- int: ca. 7
- len: 14

`technik_tueftler_21:`  Zwei Himmelsrichtungen entfernt. Nur Ost und Süd wird benutzt. 
Durchschnitt (von 20 Ausführungen) 481 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 250
- int: 100
- len: 13
- combine_numbers: 100

`technik_tueftler_22:`  Strings durch Enums ersetzt bei den Abfragen und zwei Himmelsrichtungen entfernt.
Durchschnitt (von 20 Ausführungen) 485 Aufrufe bei einem 5er Schiff. Die meisten Aufrufe:
- Random: ca. 250
- int: 100
- len: 13
- combine_numbers: 100
