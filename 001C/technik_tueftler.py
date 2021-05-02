# -*- coding: utf-8 -*-
import timeit
test_code = '''
import time
import random

MAX_SECRETS = 999 # Prio 1
MAX_PLAYTIME = 9999999 # Prio 2
MAX_KILLS = 999999 # Prio 3
multiplier_secrets = int(str(MAX_PLAYTIME) + str(MAX_KILLS))+1
multiplier_time = MAX_KILLS - 1

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s
        self.kills = kills
        self.score = 0

def sort_highscore_list_concept_1(playerlist):
    # Erstellen einer Neuen Liste bei der der Index 0 eine Score-Wertung beinhaltet und der Index 1 das Player-Objekt
    # Sortierung des Index 0 über "bubble sort" Algorithmus
    # 100   Scores: [0.0085654, 0.0016586000000000031, 0.002073499999999992, 0.001855400000000007, 0.002250199999999994, 0.002876400000000001, 0.003917000000000004, 0.0016804999999999876, 0.001510400000000009, 0.0016623000000000054]
    # 1000  Scores: [0.150328, 0.1876301, 0.17488330000000002, 0.1728246, 0.18391380000000002, 0.1752049000000001, 0.18310779999999993, 0.1782018999999999, 0.17020970000000002, 0.15676409999999996]
    # 10000 Scores: [17.7232397, 20.432162, 19.286158200000003, 16.656876200000006, 16.993382499999996, 17.31200530000001, 17.4074174, 17.5261759, 15.491052999999994, 15.382559500000013]
    extend_list = [[(temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player] for temp_player in playerlist]
    # Blasensortierung / bubble sort
    for i in range(len(extend_list)):
        for j in range(len(extend_list) - i - 1):
            if extend_list[j][0] < extend_list[j + 1][0]:
                extend_list[j], extend_list[j + 1] = extend_list[j + 1], extend_list[j]
    return [element[1] for element in extend_list]

def sort_highscore_list_concept_2(playerlist):
    # Erstellen einer Neuen Liste bei der der Index 0 eine Score-Wertung beinhaltet und der Index 1 das Player-Objekt
    # Sortierung des Index 0 über sorted und lambda
    # 100   Scores: [0.005350300000000002, 0.000627599999999999, 0.00048789999999999945, 0.0004494000000000026, 0.0005659000000000011, 0.0006871999999999989, 0.0005238000000000048, 0.0005179000000000017, 0.0007545999999999942, 0.0007759999999999989]
    # 1000  Scores: [0.011316800000000002, 0.007888500000000007, 0.005280399999999998, 0.0079177, 0.0066113999999999895, 0.006659899999999996, 0.005212099999999997, 0.006603999999999999, 0.007350099999999998, 0.006869399999999998]
    # 10000 Scores: [0.0651157, 0.050957, 0.0541692, 0.0573226, 0.05752449999999998, 0.061705399999999966, 0.06533139999999998, 0.05244269999999995, 0.051825200000000016, 0.05602380000000007]
    extend_list = [[(temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills), temp_player] for temp_player in playerlist]
    sorted_list = sorted(extend_list, key=lambda x: x[0], reverse = True)
    return [element[1] for element in sorted_list]

def sort_highscore_list_concept_3(playerlist):
    # Nutzen des Attribut "score" von Player 
    # Sortierung über den "bubble sort" Algorithmus
    # 100   Scores: 
    # 1000  Scores: 
    # 10000 Scores: 
    for temp_player in playerlist:
        temp_player.score = (temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills)
    for i in range(len(playerlist)):
        for j in range(len(playerlist) - i - 1):
            if playerlist[j].score < playerlist[j + 1].score:
                playerlist[j], playerlist[j + 1] = playerlist[j + 1], playerlist[j]  
    return playerlist

def sort_highscore_list_concept_4(playerlist):
    def get_score(player):
        return player.score
    # Nutzen des Attribut "score" von Player 
    # Sortierung über sorted und extra return Funktion
    # 100   Scores: 
    # 1000  Scores: 
    # 10000 Scores: 
    for temp_player in playerlist:
        temp_player.score = (temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills)
    return sorted(playerlist, key=get_score, reverse = True)

def sort_highscore_list_concept_5(playerlist):
    def get_score(player):
        return player.score
    # Nutzen des Attribut "score" von Player 
    # Sortierung über sorted und lambda
    # 100   Scores: 
    # 1000  Scores: 
    # 10000 Scores: 
    for temp_player in playerlist:
        temp_player.score = (temp_player.secrets*multiplier_secrets)+((MAX_PLAYTIME-temp_player.playtime_s)*multiplier_time)+(temp_player.kills)
    return sorted(playerlist, key=lambda x: x.score, reverse = True)

def get_testlist():
    test_list = []
    for i in range(100):
        test_list.append(player(str(i), random.randrange(1,100), random.randrange(1,500), random.randrange(1,1000)))
    return test_list

def main():
    #list_player_start = get_testlist()
    list_player_start = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    print("Starte Sortierung")
    sorted_list = sort_highscore_list_concept_5(list_player_start)
    for i in range(7):
        print(f'{i}: {sorted_list[i].name} mit G[{sorted_list[i].secrets}], Z[{sorted_list[i].playtime_s}], G[{sorted_list[i].kills}]')

sort_highscore_list_concept_2(get_testlist())
#main()
'''
laufzeit = timeit.Timer(test_code)
print(laufzeit.repeat(repeat=10, number=1))