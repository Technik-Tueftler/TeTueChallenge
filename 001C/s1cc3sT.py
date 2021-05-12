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
    

def sort(list_player):
    # Vielen Dank an coder2k wegen der Erklaerung der lambada-Funktion ;)
    # Sortierschlüssel in der Reihenfolge der Priorisierung. playtime mit Minus weil weniger besser ist. 
    # Reverse weil mehr secrets und kills besser sind.
    list_player_sorted = sorted(list_player, key=lambda x: (x.secrets, -x.playtime_s, x.kills), reverse=True)
    return list_player_sorted
    
    #for rank, element in enumerate(list_player_sorted, start=1):
    #    print(rank, element.name)

if __name__ == "__main__":
    main()
