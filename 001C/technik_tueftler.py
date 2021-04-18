# -*- coding: utf-8 -*-
import timeit


import time
from operator import itemgetter

multiplier_secrets = 1000000000000000 # 999000000000000000
max_time = 999999999
multiplier_time = 1000000             #    999999999000000

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s # playing time in seconds
        self.kills = kills

def main():
    sorted_list_1 = []
    list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    for rank, element in enumerate(list_player_start, start=1):
        print(rank, element.name)
    
    for temp_player in list_player_start:
        #ausgabe_list.append([temp_player.secrets*multiplier_secrets, temp_player])
        sorted_list_1.append([(temp_player.secrets*multiplier_secrets)+((max_time-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player])

    sorted_list_2 = sorted(sorted_list_1, key=itemgetter(0), reverse=True)

    for rank, element in enumerate(sorted_list_2, start=1):
        print(rank, element[1].name)

def main2():
    sorted_list_1, sorted_list_2 = []
    list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    for rank, element in enumerate(list_player_start, start=1):
        print(rank, element.name)

    #sorted_list_1 = sorted(list_player_start, key=itemgetter(0), reverse=True)
    #sorted_list_2 = sorted(sorted_list_1, key=itemgetter(1))
    sorted_list_3 = sorted(sorted(sorted(list_player_start, key=itemgetter(0), reverse=True), key=itemgetter(1)), key=itemgetter(2), reverse=True)

    for rank, element in enumerate(sorted_list_3, start=1):
        print(rank, element.name)  

if __name__ == "__main__":
    main()
