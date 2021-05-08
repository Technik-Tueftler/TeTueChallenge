# -*- coding: utf-8 -*-
import timeit

'''
Attention: to measure the runtime we use the module timeit. For this the complete code should be in a string at the end.
'''

test_code = '''
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
    
    # Vielen Dank an coder2k wegen der Erklaerung der lambada-Funktion
    list_player_sorted = sorted(list_player, key=lambda x: (x.secrets, -x.playtime_s, x.kills), reverse=True)
    
    for rank, element in enumerate(list_player_sorted, start=1):
        print(rank, element.name)

if __name__ == "__main__":
    main()

'''
laufzeit = timeit.Timer(test_code)
print(laufzeit.repeat(repeat=5, number=1))