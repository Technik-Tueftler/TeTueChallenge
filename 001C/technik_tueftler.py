# -*- coding: utf-8 -*-
"""
Provides some different kind of highscore-sort functions
sort_highscore_list_concept_1: pi(1.090), pc(0.130)
sort_highscore_list_concept_2: pi(0.039), pc(0.008)
sort_highscore_list_concept_3: pi(1.140), pc(0.151)
sort_highscore_list_concept_4: pi(0.038), pc(0.009)
sort_highscore_list_concept_5: pi(0.038), pc(0.010)
"""
import time
import random

MAX_SECRETS = 999 # Prio 1
MAX_PLAYTIME = 9999999 # Prio 2
MAX_KILLS = 999999 # Prio 3
MULTIPLIER_SECRETS = int(str(MAX_PLAYTIME) + str(MAX_KILLS))+1
MULTIPLIER_TIME = MAX_KILLS - 1

class Player:
    """
    Player class which contains player and game information
    """
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s
        self.kills = kills
        self.score = 0

def sort_highscore_list_concept_1(playerlist):
    """
    Highscore-Sort function 1
    Erstellen einer Neuen Liste bei der der Index 0 eine Score-Wertung beinhaltet und der Index 1
    das Player-Objekt
    Sortierung des Index 0 über "bubble sort" Algorithmus
    Highscore geprüft, OK
    100   Scores: pi(0.013), pc(0.002) bei 10 Wiederholungen
    1000  Scores: pi(1.090), pc(0.130) bei 10 Wiederholungen
    """
    extend_list = [
        [
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills), temp_player
        ] for temp_player in playerlist
    ]
    # Blasensortierung / bubble sort
    for i in range(len(extend_list)):
        for j in range(len(extend_list) - i - 1):
            if extend_list[j][0] < extend_list[j + 1][0]:
                extend_list[j], extend_list[j + 1] = extend_list[j + 1], extend_list[j]
    return [element[1] for element in extend_list]

def sort_highscore_list_concept_2(playerlist):
    """
    Highscore-Sort function 2
    Erstellen einer Neuen Liste bei der der Index 0 eine Score-Wertung beinhaltet und
    der Index 1 das Player-Objekt
    Sortierung des Index 0 über sorted und lambda
    Highscore geprüft, OK
    100   Scores: pi(0.004), pc(0.001) bei 10 Wiederholungen
    1000  Scores: pi(0.039), pc(0.008) bei 10 Wiederholungen
    """
    extend_list = [
        [
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills), temp_player
        ] for temp_player in playerlist
    ]
    sorted_list = sorted(extend_list, key=lambda x: x[0], reverse = True)
    return [element[1] for element in sorted_list]

def sort_highscore_list_concept_3(playerlist):
    """
    Highscore-Sort function 3
    Nutzen des Attribut "score" von Player
    Sortierung über den "bubble sort" Algorithmus
    Highscore geprüft, OK
    100   Scores: pi(0.013), pc(0.003) bei 10 Wiederholungen
    1000  Scores: pi(1.140), pc(0.151) bei 10 Wiederholungen
    """
    for temp_player in playerlist:
        temp_player.score = (
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills)
        )
    for i in range(len(playerlist)):
        for j in range(len(playerlist) - i - 1):
            if playerlist[j].score < playerlist[j + 1].score:
                playerlist[j], playerlist[j + 1] = playerlist[j + 1], playerlist[j]
    return playerlist

def sort_highscore_list_concept_4(playerlist):
    """
    Highscore-Sort function 4
    Nutzen des Attribut "score" von Player
    Sortierung über sorted und extra return Funktion
    Highscore geprüft, OK
    100   Scores: pi(0.004), pc(0.001) bei 10 Wiederholungen
    1000  Scores: pi(0.038), pc(0.009) bei 10 Wiederholungen
    """
    def get_score(player):
        return player.score

    for temp_player in playerlist:
        temp_player.score = (
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills)
        )
    return sorted(playerlist, key=get_score, reverse = True)

def sort_highscore_list_concept_5(playerlist):
    """
    Highscore-Sort function 5
    Nutzen des Attribut "score" von Player
    Sortierung über sorted und lambda
    Highscore geprüft, OK
    100   Scores: pi(0.006), pc(0.001) bei 10 Wiederholungen
    1000  Scores: pi(0.038), pc(0.010) bei 10 Wiederholungen
    """
    for temp_player in playerlist:
        temp_player.score = (
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills)
        )
    return sorted(playerlist, key=lambda x: x.score, reverse = True)

def get_testlist(quantity):
    """
    Generate a random Player test list with quantity as a parameter
    """
    test_list = []
    for i in range(quantity):
        test_list.append(
            Player(
                str(i),
                random.randrange(1,100),
                random.randrange(1,500),
                random.randrange(1,1000)
            )
        )
    return test_list

def main():
    """
    Main function to test sort functions with defined player objects
    """
    list_player_start = [
        Player("Max", 3, 50, 10),
        Player("Moritz", 2, 20, 30),
        Player("Witwe Bolte", 3, 49, 9),
        Player("Mecke", 1, 10, 79),
        Player("Lämpel", 3, 49, 10),
        Player("Fritz", 2, 20, 31),
        Player("Böck", 1, 10, 80)
    ]
    print("Starte Sortierung 1")
    sorted_list = sort_highscore_list_concept_1(list_player_start)
    for i in range(7):
        print(f'{i}: {sorted_list[i].name}')

if __name__ == "__main__":
    main()
