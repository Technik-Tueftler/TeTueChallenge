# -*- coding: utf-8 -*-
import time
import operator

MAX_SECRETS = 999
MAX_PLAYTIME = 9999999
MAX_KILLS = 999999


class Player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time() * 10000)  # create unique id
        self.name = name
        self.secrets = max(min(secrets, MAX_SECRETS), 0)
        self.playtime_s = max(min(playtime_s, MAX_PLAYTIME), 0)  # playing time in seconds
        self.kills = max(min(kills, MAX_KILLS), 0)

    @property
    def gamer_score(self):
        return (self.secrets << (len(bin(MAX_PLAYTIME)) + len(bin(MAX_KILLS)) - 4)) \
               | (max(0, (MAX_PLAYTIME - self.playtime_s)) << (len(bin(MAX_KILLS)) - 2)) \
               | self.kills


def sort_player_list(list_to_sort):
    list_to_sort.sort(key=operator.attrgetter("gamer_score"), reverse=True)


'''
to_be_sorted_list = [Player("Max", 3, 50, 10), Player("Moritz", 2, 20, 30), Player("Witwe Bolte", 3, 49, 9),
                     Player("Mecke", 1, 10, 79), Player("Lämpel", 3, 49, 10), Player("Fritz", 2, 20, 31),
                     Player("Böck", 1, 10, 80)]

sort_player_list(to_be_sorted_list)

for rank, element in enumerate(to_be_sorted_list, start=1):
    print(rank, element.name)
'''
