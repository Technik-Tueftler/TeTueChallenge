import random
import time

import curses

import os
from threading import Thread   
###################################################
# async Keypress detection 

key_pressed = False
curses.initscr()  
curses.start_color()
curses.curs_set(False)
curses.noecho()




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

class GraphicsPoint:
      def __init__(self, x, y, c, color):
            self.X = x
            self.Y = y
            self.C = c
            self.Color = color

###################################################
class MoveAbleObject:
    def __init__(self, Direction, Y): 
        self.direction = Direction
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
        self.move()
        returnPoints = []
        for p in self.points:
            returnPoints.append(GraphicsPoint((p.X + self.x_offset),(p.Y + self.y_offset), p.C, p.Color))
        return returnPoints

    
###################################################
class cloud(MoveAbleObject):

    def __init__(self, Direction, Y): 
        super().__init__(Direction, Y)
        cloudString = """
            ,((_'-. _
        _(   (_ ) ),--.
        (  (  __   _)  )-._
        """
        self.points = parseTxtToDrawableObject(cloudString) 



###################################################
class Wave(MoveAbleObject):

    def __init__(self, Direction, Y):
        super().__init__(Direction, Y)
        waveString = """
            _
            _)`'-.,_
            """
        self.points = parseTxtToDrawableObject(waveString) 





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
        self.cursesScreen = curses.newwin(curses.LINES -1 ,curses.COLS -1)
        self.cursesScreen.keypad(0)
    
    def addDrawable(self, obj):
        self.drawables.append(obj)

    def draw(self):
        self.cursesScreen.clear()
        for drawable in self.drawables:
            for p in drawable.get():
                if p.X < curses.COLS -2 and p.X >= 0:
                    self.cursesScreen.addch(p.Y, p.X, p.C, curses.color_pair(1))
        self.cursesScreen.refresh()


###################################################

class Game:

    def __init__(self):
        self.screen = Screen()
        self.water = Water()
        self.wave = Wave("left", 3)
        self.cloud = cloud("left", 7)
        self.screen.addDrawable(self.water)
        self.screen.addDrawable(self.cloud)
        self.screen.addDrawable(self.wave)


    def gameLoop(self):
        self.logicLoop()
        self.graphicsLoop()
    
    def logicLoop(self):
        if self.cloud.x_offset == -10:
            del self.cloud
            self.cloud = cloud("left", 5)
            self.screen.addDrawable(self.cloud)

    def graphicsLoop(self):
        self.screen.draw()



if __name__ == "__main__":
    thread = Thread(target = detect_key_press)
    thread.start() # keypress detection


    game = Game()

    while not key_pressed:
        game.gameLoop()
        time.sleep(0.1)
    curses.endwin()
