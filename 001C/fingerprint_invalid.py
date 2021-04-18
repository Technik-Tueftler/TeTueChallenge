import time

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets
        self.playtime_s = playtime_s # playing time in seconds
        self.kills = kills

def sortGames(unsortedList):
    sortedList=[] 
    scores = [] # a list of values representing the three dimensional highscore space as a single scalar
    for player in unsortedList: # calc the score for every player
        scores.append( player.secrets*100000000000  + 1000000/player.playtime_s + player.kills )
    while len(scores) > 0: # repeat until no player is left in list
        maxScore=max(scores) # get the maximum score
        maxIndex=scores.index(maxScore) # get the index of the max score
        sortedList.append( unsortedList[maxIndex]) # add the max score player to the output list
        unsortedList.remove( unsortedList[maxIndex]) # remove the max score player from the input list
        scores.remove(maxScore) # remove the max score from the score list
    return sortedList

def main():
    list_player = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    for rank, element in enumerate(list_player, start=1):
        print(rank, element.name)
    print('-----------')
	print('sorted Result')
	print('-----------')
    list_player_sorted = sortGames(list_player)
    for rank, element in enumerate(list_player_sorted, start=1):
        print(rank, element.name)

if __name__ == "__main__":
    main()