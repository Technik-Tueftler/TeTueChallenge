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
###################################################
class GraphicsPoint:
      def __init__(self, x, y, c, color):
            self.X = x
            self.Y = y
            self.C = c
            self.Color = color

###################################################
class Water:

    def __init__(self):
        self.toggle = 1

    def get(self):
        return self.Background()

    def toggleChar(self):
        if self.toggle == 1:
            c = '-'
            self.toggle = 0
        else:
            c = '+'
            self.toggle = 1
        return c

    def Background(self):
        c = self.toggleChar()
        background = []
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
        for y in range(curses.LINES -2):
            for x in range(curses.COLS -2):
                background.append(GraphicsPoint(x,y,c, curses.color_pair(1)))
        return background

        

###################################################

class Screen:

    def __init__(self):
        self.toggle = 1
        self.drawables = []
        self.size = os.get_terminal_size()
        self.cursesScreen = curses.initscr()
        curses.start_color()
        self.cursesScreen = curses.newwin(curses.LINES -1 ,curses.COLS -1)
        self.cursesScreen.keypad(0)
        curses.noecho()
    
    def addDrawable(self, obj):
        self.drawables.append(obj)

    def draw(self):
        self.cursesScreen.clear()
        for drawable in self.drawables:
            for p in drawable.get():
                self.cursesScreen.addch(p.Y, p.X, p.C, p.Color)
        self.cursesScreen.refresh()


###################################################

screen = Screen()
water = Water()

def gameLoop():
    screen.draw()
    
    
    
if __name__ == "__main__":
    thread = Thread(target = detect_key_press)
    thread.start() # keypress detection

    screen.addDrawable(water)

    while not key_pressed:
        gameLoop()
        time.sleep(0.5)
    curses.endwin()
