import operator
from uuid import uuid4

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = uuid4() # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s # playing time in seconds
        self.kills = kills

def main():
    
    list_player = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    
    # operator.attrgetter soll wohl schneller sein als lambda-Funktion. Hier wird die niedrigste Prioritaet zuerst sortiert.
    # Da die sorted-Methode bei gleichwertigen Attributen die Reihenfolge beibehaelt, kann mit mehrmaligem Aufruf von "unten nach oben"
    # sortiert werden (Prioritaeten). Dies fuehrt am Ende zur richtigen Reihenfolge. Glaube ich xD
    list_player_sorted = sorted(list_player, key=operator.attrgetter("kills"), reverse=True)
    list_player_sorted = sorted(list_player_sorted, key=operator.attrgetter("playtime_s"))
    list_player_sorted = sorted(list_player_sorted, key=operator.attrgetter("secrets"), reverse=True)
    
    for rank, element in enumerate(list_player_sorted, start=1):
        print(rank, element.name)

if __name__ == "__main__":
    main()
