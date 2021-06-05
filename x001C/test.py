# -*- coding: utf-8 -*-
# pylint x001C/technik_tueftler.py
import timeit, time, operator
import technik_tueftler
import s1cc3sT, korbi_korb, fingerprint_invalid

players = technik_tueftler.get_testlist(100000)
list_1 = players[:]
list_2 = players[:]
list_3 = players[:]
list_4 = players[:]
list_5 = players[:]
num_runs = 1
num_repetions = 10
MAX_SECRETS = 999
MAX_PLAYTIME = 9999999
MAX_KILLS = 999999
MULTIPLIER_SECRETS = int(str(MAX_PLAYTIME) + str(MAX_KILLS))+1
MULTIPLIER_TIME = MAX_KILLS - 1


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


list_player = [Player("Max", 3, 50, 10), Player("Moritz", 2, 20, 30), Player("Witwe Bolte", 3, 49, 9), Player("Mecke", 1, 10, 79), Player("Lämpel", 3, 49, 10), Player("Fritz", 2, 20, 31), Player("Böck", 1, 10, 80)]


def sort_highscore_list_concept_5():
    """
    Technik_Tueftler
    """
    for temp_player in players:
        temp_player.score = (
            (temp_player.secrets*MULTIPLIER_SECRETS) +
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME) +
            (temp_player.kills)
        )
    return sorted(list_1, key=lambda x: x.score, reverse=True)


def sort_highscore_list_concept_6():
    """
    Highscore-Sort function 5
    Nutzen des Attribut "score" von Player
    Sortierung über sorted und lambda
    Highscore geprüft, OK
    100   Scores: pi(0.006), pc(0.001) bei 10 Wiederholungen
    1000  Scores: pi(0.038), pc(0.010) bei 10 Wiederholungen
    """
    for temp_player in list_5:
        temp_player.score = (
            (temp_player.secrets*MULTIPLIER_SECRETS)+
            ((MAX_PLAYTIME-temp_player.playtime_s)*MULTIPLIER_TIME)+
            (temp_player.kills)
        )
    return sorted(list_5, key=operator.attrgetter("score"), reverse = True)


def s1cc3sT():
    """
    s1cc3sT
    """
    # list_player_sorted = sorted(list_2, key=lambda x: (
    #     x.secrets, -x.playtime_s, x.kills), reverse=True)
    '''
    '''
    list_player_sorted = sorted(list_2, key=operator.attrgetter("kills"), reverse=True)
    list_player_sorted = sorted(list_player_sorted, key=operator.attrgetter("playtime_s"))
    list_player_sorted = sorted(list_player_sorted, key=operator.attrgetter("secrets"), reverse=True)
    return list_player_sorted


def sortGames():
    """
    fingerprint_invalid
    """
    sortedList = [] 
    scores = []  # a list of values representing the three dimensional highscore space as a single scalar
    for player in list_4: # calc the score for every player
        scores.append(player.secrets*10000000000000  + 9999999000000/player.playtime_s + player.kills )
    while len(scores) > 0: # repeat until no player is left in list
        maxScore=max(scores) # get the maximum score
        maxIndex=scores.index(maxScore) # get the index of the max score
        sortedList.append( list_4[maxIndex]) # add the max score player to the output list
        list_4.remove( list_4[maxIndex]) # remove the max score player from the input list
        scores.remove(maxScore) # remove the max score from the score list
    return sortedList


def sort_player_list():
    """
    korbi_korb
    """
    list_3.sort(key=operator.attrgetter("gamer_score"), reverse=True)


ex_time = timeit.Timer(s1cc3sT).repeat(
        repeat=num_repetions, number=num_runs)
print(f'{"s1cc3sT:":<25}{min(ex_time):.3f}s')

ex_time = timeit.Timer(sort_player_list).repeat(
        repeat=num_repetions, number=num_runs)
print(f'{"korbi_korb:":<25}{min(ex_time):.3f}s')

ex_time = timeit.Timer(sort_highscore_list_concept_5).repeat(
        repeat=num_repetions, number=num_runs)
print(f'{"Technik_Tueftler:":<25}{min(ex_time):.3f}s')

ex_time = timeit.Timer(sortGames).repeat(
        repeat=num_repetions, number=num_runs)
print(f'{"fingerprint_invalid:":<25}{max(ex_time):.3f}s')
