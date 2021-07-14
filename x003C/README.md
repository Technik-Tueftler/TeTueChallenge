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
6. Der letzte Commit muss bis 13.07.2021 20:00 Uhr gepushed sein.
7. Bitte die fertig entwickelten Funktionen, welche ihr freigeben wollt, in die source/__init__.py eintragen.

## Aufgabe
Die Aufgabe ist diesmal eine kreative. Als Vorbereitung auf ein kleines Schiffe versenken Spiel, soll eine Funktion
erstellt werden, welche den grafischen Output erstellt. Das Spielfeld sollte flexibel erstellt werden über x*x. Wird das
File ausgeführt, soll das Spielfeld aufgebaut werden. Hier ist eure Kreativität gefragt. Easter-Eggs sind natürlich 
gerne gesehen. Ob ihr das Ganze nur mit [print] Anweisungen oder mit einem Modul wie [rich] erstellt, ist euch 
überlassen. Einzige Bedingung wäre, dass es über ein File ausführbar wird (source-file oder test-file) und nur print
oder rich benutzt wird.

## Zusatzaufgabe
Nach dem ersten Print, soll ein Eingabefenster in der Konsole die Koordinate abfragen, auf die geschossen werden soll.
Danach soll eine neue Ausgabe des Feldes kommen, auf dem das angegebene Feld optisch verändert wird. 

## Hilfe zu Rich
GitHub: https://github.com/willmcgugan/rich
Soweit ich das gesehen habe, geht die Rich-Ausgabe nicht über die PyCharm Konsole. Ausführen könnt ihr das Ganze aber 
über die Windowskonsole.
1. Konsole öffnen
2. In das Projektverzeichnis TeTueChallenge wechseln
3. Entwicklungsumgebung aktivieren über:
```venv\Scripts\activate```
jetzt kann man in den jeweiligen Ordner wechseln und den Code ausführen über:
```python technik_tueftler.py```

## Fehlerbehandlung
Da es rein um die Aufgabe geht und den Lösungsweg, vernachlässigen wir die Fehlerbehandlung. 
Es wird immer davon ausgegangen, dass die übergebenen Parameter im korrekten Wertebereich sind und der übergebene
Pfad existiert.

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch. Ich bin kein Profi in Python und will 
mit euch die Kriterien für die Bewertung gemeinsam machen. Diese können sich jederzeit ändern. Also bleibt auf dem 
Laufenden. Grundlegend stelle ich mir die Abstufungen aber wie folgt vor:
1. Aufgabe erfüllt/nicht erfüllt
2. Anforderungen erfüllt und umgesetzt
~~3. Verständlicher Code (für mich und dem Chat, Kommentare usw.)~~
~~4. Laufzeit (je schneller, desto besser)~~
5. Nachinstallierte Module über requirements (je weniger, desto besser)
~~6. Zeilenanzahl (je weniger, desto besser)~~

# Ergebnisse
