import time
import random

class player:
    def __init__(self, name, secrets=0, playtime_s=0, kills=0):
        self.gameid = int(time.time()*10000) # create unique id
        self.name = name
        self.secrets = secrets # max 999
        self.playtime_s = playtime_s # max 9,999,999
        self.kills = kills # max 999,999

def sortGames(unsortedList):
    sortedList=[] 
    scores = [] # a list of values representing the three dimensional highscore space as a single scalar
    for player in unsortedList: # calc the score for every player
        scores.append( player.secrets*10000000000000  + 9999999000000/player.playtime_s + player.kills )
    while len(scores) > 0: # repeat until no player is left in list
        maxScore=max(scores) # get the maximum score
        maxIndex=scores.index(maxScore) # get the index of the max score
        sortedList.append( unsortedList[maxIndex]) # add the max score player to the output list
        unsortedList.remove( unsortedList[maxIndex]) # remove the max score player from the input list
        scores.remove(maxScore) # remove the max score from the score list
    return sortedList

def main():
    test_list = [player("Max", 3, 50, 10), player("Moritz", 2, 20, 30), player("Witwe Bolte", 3, 49, 9), player("Mecke", 1, 10, 79), player("Lämpel", 3, 49, 10), player("Fritz", 2, 20, 31), player("Böck", 1, 10, 80)]
    
    print('-----------')
    print('sorted Result')
    print('-----------')
    test_list_sorted = sortGames(test_list)
    for rank, element in enumerate(test_list_sorted, start=1):
        print(rank, element.name)

    print('-----------')
    print('Performance test')
    print('-----------')

    PerformanceListSize = 1000 # how many items are in the list to be sorted
    PerformanceAttempts = 100 # how many time the algo is executed to try to get the best result

    times = []
    for i in range(PerformanceAttempts):
        test_list = [] # list creation slightly modified to include given max values  
        for i in range(PerformanceListSize):
            test_list.append(player(str(i), random.randrange(1,999), random.randrange(1,9999999), random.randrange(1,999999)))
        startTime=time.monotonic_ns() # aquire starting time
        test_list_sorted = sortGames(test_list) # do the thing
        endTime = time.monotonic_ns() # aquire endtime
        diff = endTime-startTime 
        times.append(diff) # make a list of times the algo has taken

    minimumTime = min(times) # get min because thats the best :D
    print('Minimum time taken for sorting the performance test list: ' + str(minimumTime/1000000) + 'ms')
    print("List Size: " + str(PerformanceListSize))
    print("Attempts for minimum execution time: " + str(PerformanceAttempts))
    print()

if __name__ == "__main__":
    main()