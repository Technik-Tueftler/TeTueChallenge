#from uuid import uuid4
import time

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s # playing time in seconds
        self.kills = kills


def main():
    
    list_player = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    
    # thanks to coder2k for explaining lambda functions
    list_player_sorted = sorted(list_player, key=lambda x: (x.secrets, -x.playtime_s, x.kills), reverse=True)
    
    for rank, element in enumerate(list_player_sorted, start=1):
        print(f"{rank} {element.name} {element.gameid}")

if __name__ == "__main__":
    main()
