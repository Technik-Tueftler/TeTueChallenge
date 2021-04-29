# -*- coding: utf-8 -*-
import timeit
import time
import random
from operator import itemgetter

multiplier_secrets = 1000000000000000 # 999000000000000000
max_time = 999999999
multiplier_time = 1000000             #    999999999000000

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets # min, max, resolution
        self.playtime_s = playtime_s # min, max, resolution
        self.kills = kills # min, max, resolution

def sort_highscore_list(playerlist):
    multiplier_secrets = 1000000000000000 # 999000000000000000
    max_time = 999999999
    multiplier_time = 1000000             #    999999999000000
    sorted_list = []
    test = 0
    start = time.time()
    extend_list = [[(temp_player.secrets*multiplier_secrets)+((max_time-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player] for temp_player in playerlist]
    # Blasensortierung / bubble sort
    for i in range(len(extend_list)):
        ## iterating from 0 to n-i-1 as last i elements are already sorted
        for j in range(len(extend_list) - i - 1):
            ## checking the next element
            print(test)
            if extend_list[j][0] < extend_list[j + 1][0]:
                test = test +1
                ## swapping the adjucent elements
                extend_list[j], extend_list[j + 1] = extend_list[j + 1], extend_list[j]
    end = time.time()
    print(f'Dauer der Funktion <sort_highscore_list> beträgt {end - start} Sekunden.')
    return extend_list

def get_testlist():
    test_list = []
    start = time.time()
    for i in range(100):
        test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
    end = time.time()
    return test_list

def main():
    list_player_start = get_testlist()
    #list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]

    sorted_list = sort_highscore_list(list_player_start)
    for i in range(7):
        print(f'{i}: {sorted_list[i][1].name} mit G[{sorted_list[i][1].secrets}], Z[{sorted_list[i][1].playtime_s}], G[{sorted_list[i][1].kills}]')
    
if __name__ == "__main__":
    main()
