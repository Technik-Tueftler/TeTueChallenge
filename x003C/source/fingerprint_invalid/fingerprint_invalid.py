import random
import time

import curses

import os
from threading import Thread   
###################################################
# async Keypress detection 

key_pressed = False

def detect_key_press():
    global key_pressed
    stdscr = curses.initscr()
    key = stdscr.getch()
    key_pressed = True
    endCurses()


###################################################

def endCurses():
    curses.nocbreak()
    stdscr = curses.initscr()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

#screen.getch()

#curses.endwin()

class Screen:

    def __init__(self):
        self.toggle = 1
        self.size = os.get_terminal_size()
        self.cursesScreen = curses.initscr()
        curses.start_color()
        self.cursesScreen = curses.newwin(curses.LINES -1 ,curses.COLS -1)
        self.cursesScreen.keypad(0)
        curses.noecho()
        
    def toggleChar(self):
        if self.toggle == 1:
            c = '-'
            self.toggle = 0
        else:
            c = '+'
            self.toggle = 1
        return c

    def draw(self):
        c = self.toggleChar()
        self.cursesScreen.clear()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
        for y in range(curses.LINES -2):
            for x in range(curses.COLS -2):
                self.cursesScreen.addch(y,x, c, curses.color_pair(1))
        self.cursesScreen.refresh()

###################################################

screen = Screen()

def gameLoop():
    screen.draw()
    
    
    
if __name__ == "__main__":
    thread = Thread(target = detect_key_press)
    thread.start() # keypress detection

    while not key_pressed:
        gameLoop()
        time.sleep(0.2)
    curses.endwin()
