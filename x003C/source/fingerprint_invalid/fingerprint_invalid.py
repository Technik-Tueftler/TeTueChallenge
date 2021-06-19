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

def parseTxtToDrawableObject(parseString):
    x = 0
    y = -1
    points = []
    for c in parseString:
        if c != " " and c != "\n":
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
            points.append(GraphicsPoint(x, y, c , curses.color_pair(1) ))
            x = x + 1
        else: 
            if c == "\n":
                x = 0
                y = y + 1
    return points

###################################################



def endCurses():
    curses.nocbreak()
    stdscr = curses.initscr()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
###################################################

class Wave():

    def __init__(self, Direction, Y):
        waveString = """
            _
            _)`'-.,_
            """
        self.direction = Direction
        self.points = parseTxtToDrawableObject(waveString) 
        if Direction == "left":
            self.x_offset = curses.COLS + 8
        if Direction == "right":
            self.x_offset = -5
        self.y_offset = Y
        self.cnt = 0

    def move(self):
        if self.direction == "left":
            self.x_offset = self.x_offset - 1
        else:
            if self.direction == "right":
                self.x_offset = self.x_offset + 1


    def get(self):
        if self.cnt == 0:
            self.cnt = 0
            self.move()
        else:
            self.cnt += 1
        returnPoints = []
        for p in self.points:
            returnPoints.append(GraphicsPoint((p.X + self.x_offset),(p.Y + self.y_offset), p.C, p.Color))
        return returnPoints
    
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
        pass

    def get(self):
        return self.Background()

    def Background(self):
        c = ' '
        background = []
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        for y in range(curses.LINES -2):
            for x in range(curses.COLS -2):
                background.append(GraphicsPoint(x, y, c, curses.color_pair(1)))
        return background

        

###################################################

class Screen:

    def __init__(self):
        self.drawables = []
        self.size = os.get_terminal_size()
        self.cursesScreen = curses.initscr()
        curses.start_color()
        curses.curs_set(False)
        self.cursesScreen = curses.newwin(curses.LINES -1 ,curses.COLS -1)
        self.cursesScreen.keypad(0)
        curses.noecho()
    
    def addDrawable(self, obj):
        self.drawables.append(obj)

    def draw(self):
        self.cursesScreen.clear()
        for drawable in self.drawables:
            for p in drawable.get():
                if p.X < curses.COLS -1:
                    self.cursesScreen.addch(p.Y, p.X, p.C, curses.color_pair(1))
 
        

        self.cursesScreen.refresh()


###################################################

screen = Screen()
water = Water()
wave1 = Wave("left", 5)

def gameLoop():
    screen.draw()
    
    
    
if __name__ == "__main__":
    thread = Thread(target = detect_key_press)
    thread.start() # keypress detection

    screen.addDrawable(water)
    screen.addDrawable(wave1)

    while not key_pressed:
        gameLoop()
        time.sleep(0.1)
    curses.endwin()
