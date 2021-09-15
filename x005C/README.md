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
6. Der letzte Commit muss bis 13.10.2021 19:00 Uhr gepushed sein.
7. Bitte die fertig entwickelten Funktionen, welche ihr freigeben wollt, in die source/__init__.py eintragen.

## Aufgabe
Die Aufgabe ist eine Erweiterung aus der Challenge 3 und soll unser Spiel Schiffeversenken erweitern. Schreibt eine Funktion, die ein Schiff, zufällig, in das Spielfeld einfügt. Die nachfolgenden Regeln sollten erfüllt sein:
1. Die Felder müssen frei sein und dürfen nicht durch ein anderes Schiff belegt sein.
2. Legale Schiffspositionen sind nur waagerecht und senkrecht. Also keine Diagonalen.
3. In die Liste soll einfach ein X eingetragen werden für ein belegtes Feld.

Die Funktion sollte so aufgerufen werden:
```python
def set_new_battleship(battlefield: list, ship_size: int) -> None:
    pass
```
**battlefield:** ist die zweidimensionale Liste. Diese könnt ihr so generieren:
```python
battlefield = [[0] * 10 for i in range(10)]
```
**ship_size:** ist die Schiffslänge. Die sollte nicht kleiner sein als 3 und nicht größer als 5.



## Fehlerbehandlung
Da es rein um die Aufgabe geht und den Lösungsweg, vernachlässigen wir die Fehlerbehandlung. 
Es wird immer davon ausgegangen, dass die übergebenen Parameter im korrekten Wertebereich sind und der übergebene
Pfad existiert.

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch. Grundlegend stelle ich mir die Abstufungen aber wie folgt vor:
1. Aufgabe erfüllt/nicht erfüllt
2. Anforderungen erfüllt und umgesetzt

## Ergebnisse