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
import random
test_list = []
for i in range(1000):
    test_list.append(Player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))

sort_player_list(test_list)

for rank, element in enumerate(test_list, start=1):
    print(rank, element.name)



max_kills_player = Player("Max_secrets", MAX_SECRETS, 0, MAX_KILLS)
gamerscore = max_kills_player.gamer_score
print(len(bin(gamerscore)))

'''
