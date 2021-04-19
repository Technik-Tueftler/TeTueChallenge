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

def get_testlist():
    test_list = []
    start = time.time()
    for i in range(100000):
        test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
    end = time.time()
    #print(f'Liste mit {len(test_list)} Einträgen erstellt in {end - start} Sekunden')

    return test_list

    # start = time.time()
    # test_list_2 = [player(str(i), random.randrange(1,1000), random.randrange(1,1000), random.randrange(1,1000)) for i in range(10000)]
    # end = time.time()
    # print(end - start)
    # print(len(test_list_2))

def main1():
    sorted_list_1 = []
    list_player_start = get_testlist()
    # list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    # for rank, element in enumerate(list_player_start, start=1):
    #     print(rank, element.name)
    
    start = time.time()
    sorted_list_1 = [[(temp_player.secrets*multiplier_secrets)+((max_time-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player] for temp_player in list_player_start]
    # for temp_player in list_player_start:
    #     sorted_list_1.append([(temp_player.secrets*multiplier_secrets)+((max_time-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player])

    #sorted_list_2 = sorted(sorted_list_1, key=itemgetter(0), reverse=True)
    #sorted_list_2 = sorted(sorted_list_1, key=lambda x:x[0], reverse=True)
    sorted_list_2 = sort(sorted_list_1)
    end = time.time()
    print(end - start)

    for i in range(10):
        print(f'{i}: {sorted_list_2[i][1].name} mit G[{sorted_list_2[i][1].secrets}], Z[{sorted_list_2[i][1].playtime_s}], G[{sorted_list_2[i][1].kills}]')

    # for rank, element in enumerate(sorted_list_2, start=1):
    #     print(rank, element[1].name)

def main2():
    sorted_list_1 = []
    sorted_list_2 = []
    list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    for rank, element in enumerate(list_player_start, start=1):
        print(rank, element.name)

    start = time.time()
    sorted_list_1 = sorted(list_player_start, key=itemgetter(0), reverse=True)
    sorted_list_2 = sorted(sorted_list_1, key=itemgetter(1))
    sorted_list_3 = sorted(sorted_list_2, key=itemgetter(2), reverse=True)
    end = time.time()
    print(end - start)
    for rank, element in enumerate(sorted_list_3, start=1):
        print(rank, element.name)  
    
if __name__ == "__main__":
    main1()
    #get_testlist()