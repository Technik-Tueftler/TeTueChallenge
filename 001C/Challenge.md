# DE
## Weitere Regeln
- Python 3.8.x
- Du kannst auch gerne die Aufgabe in einer anderen Sprache lösen. Die werden wir aber nicht on-stream besprechen und uns ansehen. Vorrangig wollen wir hier Python lernen. Im PR kannst du aber gerne einen Screenshot anhängen, der zeigt, dass dein Code ebenfalls funktioniert.
- Nur ein File mit dem Twitchnamen (Beispiel: technik_tueftler.py).
- Grundlegende Struktur des Codes siehe technik_tueftler.py.
- Gestartet wird die Challenge am 14.04.2021 im Stream.
- Der letzte Commit muss bis 12.05.2021 19:30 Uhr gepushed sein.
- Für den ersten Versuch zum messen der Laufzeit benutzen wir das Modul timeit. Dazu sollte der komplette Code am Ende in einem String stehen.
- Die Klasse **player** kann gerne erweitert werden um ein Attribute oder eine Funktion.
## Aufgabe
Für ein Spiel entwickel eine Modul (ein Python-File) was eine sortierte Liste für einen Highscore zurückgibt. Die sortierte Liste soll wieder die entgegengenommenen Objekte zurückgeben. Die Objekte sind beendete Spiele mit verschiedenen Attributen. Die Spieler (Objekte) sollen wie folgt sortiert und priorisiert werden:  
1. secrets in aufsteigender Reihenfolge (je mehr secrets desto besser)
--> Hier kann für eine bessere Optimierung ein Maximalwert von 999 angenommen werden.
2. playtime_s in absteigender Reihenfolge (je weniger Zeit gebraucht wurde desto besser)
--> Hier kann für eine bessere Optimierung ein Maximalwert von 9.999.999 angenommen werden.
3. kills in aufsteigender Reihenfolge (je mehr kills desto besser)  
--> Hier kann für eine bessere Optimierung ein Maximalwert von 999.999 angenommen werden.
**Übergabe einer unsortierten Liste:** [<player_1>, <player_2>, <player_n>]  
**Rückgabe einer sortierten Liste:** [<player_2>, <player_1>, <player_n>]  
## Test
Für den Highscore ist eine Optimierung für Datensätze bis maximal 1000 Objekte Sinnvoll. Der Algorithmus kann also gerne auf diese Maximalmenge angepasst und optimiert werden.
### Test Daten für Sortierung
```python
test_list = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
```
### Test Daten für Performace
```python
test_list = []
for i in range(1000):
    test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
```
### Print-Function
```python
for rank, element in enumerate(list_player, start=1):
    print(rank, element.name)
```
### Ausgabe unsortiert
```
1 Max
2 Moritz
3 Witwe Bolte
4 Mecke
5 Lämpel
6 Fritz
7 Böck
```
### Ausgabe sortiert
```
1 Lämpel
2 Witwe Bolte
3 Max
4 Fritz
5 Moritz
6 Böck
7 Mecke
```

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch. Ich bin kein Profi in Python und will mit euch die Kriterien für die Bewertung gemeinsam machen. Diese können sich jederzeit ändern. Also bleibt auf dem laufenden. Grundlegend stelle ich mir die Abstufungen aber wie folgt vor:
1. Aufgabe erfüllt/nicht erfüllt
2. Laufzeit (je schneller desto besser)
3. Nachinstallierte Module über requirements (je weniger desto besser)
4. Zeilenanzahl (je weniger desto besser)
~~5. Sauberer Code (aktueller PEP 8)~~
5. Verständlicher Code (für mich und dem Chat)

# Ergebnisse
1. Aufgabe erfüllt/nicht erfüllt
1.1 s1cc3sT
1.1.1 s1cc3sT           --> i.O.
1.1.2 s1cc3sT_2         --> i.O.
1.2 korbi_korb          --> i.O.
1.3 fingerprint_invalid --> i.O.
1.4 helbaco             --> n.i.O
2. Laufzeit
2.1 s1cc3sT
2.1.1 s1cc3sT           -->    0.839s (100.000 Einträgen)
2.1.2 s1cc3sT_2         -->    0.584s (100.000 Einträgen)
2.2 korbi_korb          -->    1.002s (100.000 Einträgen)
2.3 fingerprint_invalid --> 1831.867s (100.000 Einträgen)
2.4 helbaco             --> N.A.
3. Nachinstallierte Module
3.1 s1cc3sT
3.1.1 s1cc3sT           --> Keine
3.1.2 s1cc3sT_2         --> Operator (Optimierung der Performance)
3.2 korbi_korb          --> Operator (Optimierung der Performance)
3.3 fingerprint_invalid --> Keine
3.4 helbaco             --> Keine
4. Zeilenanzahl
4.1 s1cc3sT
4.1.1 s1cc3sT           -->  1
4.1.2 s1cc3sT_2         -->  3
4.2 korbi_korb          -->  2
4.3 fingerprint_invalid --> 11
4.4 helbaco             -->  3
5. Verständlicher Code
5.1 s1cc3sT
5.1.1 s1cc3sT
(+) Beschreibung was passiert in der Funktion. Eventuell nochmal Kurzbeschreibung was macht die Funktion.
(+) Eine Zeile Code, maximale Vereinfachung.
(-) Schön wäre es gewesen, wenn es eine eigene Funktion bekommen hätte und nicht in der Main Funktion stehen würde. Eigener return value und übergabe der Liste im Funktionsaufruf. 
5.1.2 s1cc3sT_2
(+) Beschreibung was passiert in der Funktion. Eventuell nochmal Kurzbeschreibung was macht die Funktion.
(+) Wenige Zeilen Code mit selbem Inhalt. Einfache Schreibweise, einfach anzupassen.
(-) Schön wäre es gewesen, wenn es eine eigene Funktion bekommen hätte und nicht in der Main Funktion stehen würde. Eigener return value und übergabe der Liste im Funktionsaufruf. 
5.2 korbi_korb
(+) Richtig cool Idee über Bitshift die Konstanden einzubauen. So entfällt eine Umrechung und ist direkt verknüpft mit den Konstanden und keiner Umrechunung mehr.
(+) Um die Geschwindigkeit zu erhöhen nochmal mit dem operator gearbeitet.
(+) Ausfführliche Tests und Beschreibungen der Ideen.
(+) Im Init der Klasse, Schutz für Fehleingabe.
(-) Kleine Beschreibung der Funktion im Code.
5.3 fingerprint_invalid
(+) Durchläuft man die Liste zweimal hintereinander (nachdem schon mal sortiert wurde) wird der zweite Durchlauf in 0 Sekunden durchlaufen, da schon sortiert ist.
(+) Eigene Umsetzung angelehnt an C ohne Hilfsfunktionen.
(+) Zeilengenaue Beschreibung der Funktion.
(+) Liste wird an die Funktion übergeben und es wird eine andere Liste zurückgegeben.
(-) Kleine Beschreibung der Funktion im Code.
(-) Division durch null möglich.
5.4 helbaco
(+) Wenige Zeilen Code mit selbem Inhalt. Einfache Schreibweise, einfach anzupassen.
(-) Es wird nicht sortiert.

# EN
## Further rules
- Python 3.8.x
- Only one file with the twitchname (example: technik_tueftler.py).
- Basic structure of the code see technik_tueftler.py.
- The Challenge will be launched on 14.04.2021 on stream.
- The last commit must be pushed by 12.05.2021 19:30.
- For the first attempt to measure the runtime we use the module timeit. For this the complete code should be in a string at the end. 
- The class **player** can be extended with an attribute or a function.
## Challenge
Develop (for a game) a module (a Python file) which returns a sorted list for a highscore. The sorted list should return the input objects. The objects are finished games with different attributes. The players (objects) shall be sorted and prioritized as follows:  
1. secrets in ascending order (more secrets, better).  
--> A maximum value of 999 can be assumed here for better optimization.
2. playtime_s in descending order (less time, better)  
--> A maximum value of 9,999,999 can be assumed here for better optimization.
3. kills in ascending order (more kills, better)  
--> A maximum value of 999,999 can be assumed here for better optimization.
**Handing over an unsorted list:** [<player_1>, <player_2>, <player_n>]  
**Return of a sorted list:** [<player_2>, <player_1>, <player_n>]  
## Test
For the highscore, an optimization for data sets up to a maximum of 1000 objects makes sense. The algorithm can therefore be adapted and optimized to this maximum quantity.
### Test data for sorting
```python
test_list = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
```
### Test data for performace
```python
test_list = []
for i in range(1000):
    test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
```
### Print-Function
```python
for rank, element in enumerate(list_player, start=1):
    print(rank, element.name)
```
### Output unsorted
```
1 Max
2 Moritz
3 Witwe Bolte
4 Mecke
5 Lämpel
6 Fritz
7 Böck
```
### Output sorted
```
1 Lämpel
2 Witwe Bolte
3 Max
4 Fritz
5 Moritz
6 Böck
7 Mecke
```

## Rating
In the first place is the fun and a common solution at the end with you. I'm not a pro in Python and want to share with you the criteria for rating. These are subject to change at any time. So stay tuned for updates. But basically I imagine the gradations as follows:
1. task completed/not completed
2. runtime (the faster the better)
3. post-installed modules over requirements (the less the better)
4. number of lines (the less the better)
5. clean code (current PEP 8)
6. understandable code (for me and the chat)
