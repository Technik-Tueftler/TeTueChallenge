# -*- coding: utf-8 -*-
import timeit
import time
import random
from operator import itemgetter

MAX_SECRETS = 999 # Prio 1
MAX_PLAYTIME = 9999999 # Prio 2
MAX_KILLS = 999999 # Prio 3

multiplier_secrets = int(str(MAX_PLAYTIME)+ str(MAX_KILLS))+1
multiplier_time = MAX_KILLS - 1

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s
        self.kills = kills
        self.score = 0

def sort_highscore_list(playerlist):
    start = time.time()
    extend_list = [[(temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player] for temp_player in playerlist]
    # Blasensortierung / bubble sort
    for i in range(len(extend_list)):
        for j in range(len(extend_list) - i - 1):
            if extend_list[j][0] < extend_list[j + 1][0]:
                extend_list[j], extend_list[j + 1] = extend_list[j + 1], extend_list[j]
    end = time.time()
    print(f'Dauer der Funktion <sort_highscore_list> beträgt {end - start} Sekunden.')
    return extend_list

def sort_highscore_list_2(playerlist):
    for temp_player in playerlist:
        temp_player.score = (temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills)
#    return sorted(playerlist, key=get_score, reverse = True)
    for i in range(len(playerlist)):
        for j in range(len(playerlist) - i - 1):
            if playerlist[j].score < playerlist[j + 1].score:
                playerlist[j], playerlist[j + 1] = playerlist[j + 1], playerlist[j]  
    return playerlist

def get_score(player):
        return player.score

def get_testlist():
    test_list = []
    start = time.time()
    for i in range(1000):
        test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
        #test_list.append(player(str(i), random.randrange(1,1000), random.randrange(1,10000000), random.randrange(1,1000000)))
    end = time.time()
    return test_list

def main():
    list_player_start = get_testlist()
    #list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    print("Starte Sortierung")
    start = time.time()
    sorted_list = sort_highscore_list_2(list_player_start)
    end = time.time()
    print(f'Dauer der Funktion <sort_highscore_list> beträgt {end - start} Sekunden.')
    for i in range(7):
        print(f'{i}: {sorted_list[i].name} mit G[{sorted_list[i].secrets}], Z[{sorted_list[i].playtime_s}], G[{sorted_list[i].kills}]')

if __name__ == "__main__":
    main()
