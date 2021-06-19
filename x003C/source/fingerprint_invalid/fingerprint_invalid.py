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
        #self.cursesScreen = curses.newwin(self.size.lines,self.size.columns)
        self.cursesScreen.keypad(0)
        curses.noecho()
        
    def toggleScreen(self):
        self.lines = [] 
        if self.toggle == 1:
            c = '-'
            self.toggle = 0
        else:
            c = '+'
            self.toggle = 1
        for _ in range(self.size.lines):
            line = [c] * (self.size.columns - 1)
            self.lines.append(line)

    def draw(self):
        self.toggleScreen()
        self.cursesScreen.clear()
        for line in self.lines:
            line = ''.join(line)
            l = len(line)
            self.cursesScreen.addstr((line))
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
        time.sleep(1)
    curses.endwin()
