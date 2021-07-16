# DE
Erstelle ein Overlay für mein Streamdeck, welches bei jedem Stream zufällig aus allen Einsendungen gestartet wird. 
Die Aufgabe ist wieder eine kreative Aufgabe. Mit welchem Modul oder welches Design ihr wählt ist Grundsätzlich egal. 
Also Konsolen-GUIs (z.B. https://github.com/willmcgugan/textual), QT5 oder Tkinter kann alles benutzt werden.

## Anforderungen (Weitere Regeln)
1. Die Funktionen müssen unter Python 3.8 laufen und auf einem Raspberry Pi Zero (Raspbian Pi OS) (ihr könnt das Overlay aber auch unter Windows starten und testen. Das hatte bei mir auch geklappt und müsst keinen Pi und Touchdisplay kaufen. 
2. Maximal zwei Dateien erlaubt. Funktionsfile und ein Testfile in den jeweiligen Ordnern.
3. Der Start des Overlays soll über ein *.py gestartet werden können.
4. Das File mit den Funktionen muss unter *source* abgelegt werden mit dem Dokumentenname *twitchname*.py
   in Kleinbuchstaben. Weitere Informationen, Ideen und Anmerkungen jeweils im Modul mit
   Kommentaren einfügen und dokumentieren.
5. Ein Testfile unter *test* mit dem Namen *twitchname*_test.py in Kleinbuchstaben, falls benötigt.
6. Der letzte Commit muss bis 17.08.2021 20:00 Uhr gepushed sein.
7. Das Overlay soll für ein Display mit 800x480 ausgelegt und optimiert sein.
8. Tabs sollen möglich sein, dass die Buttons möglichst groß gewählt werden können.
9. Auf der Auflösung sind 4x2 Buttons recht einfach zu drücken mit den Fingern, es sollten daher nicht mehr Buttons vorgesehen werden.
10.Die Bilddateien (falls gebraucht) sollen im Ordner media liegen und von dort aus benutzt werden.


## Zusatzaufgabe
1. Button betätigung sollte ein Testereignis ausführen
2. Togglebutton einbauen. Also erste Betätigung Bild wechseln und Aufruf einer testfunc1(), nochmal drücken Anfangsbild und Aufruf einer testfunc2()
3. Farbschema soll angenhem sein. Aktuelles Farbschema ist: #1a1a1a, #333333, #808080, #aa302f, #f8792a, #a02c2c und #c87137

## Fehlerbehandlung
Da es rein um die Aufgabe geht und den Lösungsweg, vernachlässigen wir die Fehlerbehandlung. 
Es wird immer davon ausgegangen, dass die übergebenen Parameter im korrekten Wertebereich sind und der übergebene
Pfad existiert.

## Bewertung
An erster Stelle steht der Spaß und eine gemeinsame Lösung am Ende mit euch.
