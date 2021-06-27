import locale
import time
import sys
import curses
import random
import os
from threading import Thread  
from curses import wrapper as cursesWrapper
###################################################
class KeyboardController():
    
    def __init__(self):
        thread = Thread(target = self.detect_key_press)
        thread.start()
        self.key_pressed = False


    def detect_key_press(self):
        self.key_pressed = False
        stdscr = curses.initscr()
        self.key = stdscr.getch()
        self.key_pressed = True

    def getKey(self):
        thread = Thread(target = self.detect_key_press)
        thread.start()
        return self.key

    def getKeyPressed(self):
        return self.key_pressed




###################################################
chickenString = (
r"             xx     \n"
r"             / .|_  \n"
r"            /(_)_<  \n"
r"           /  (     \n"
r"  ((____.-'    )    \n"
r"   \\          /    \n"
r"    \\'-.-.-'`/     \n"
r"     \\______/      \n"
r"       _|_\\_         "
)

tetueString = (
r'\__   __/(  ____ \ __   __/|\     /|(  ____ \    (  ____ \|\     /|(  ___  )( \      ( \      (  ____ \( (    /|(  ____ \(  ____ \ \n'
r'   ) (   | (    \/   ) (   | )   ( || (    \/    | (    \/| )   ( || (   ) || (      | (      | (    \/|  \  ( || (    \/| (    \/ \n'
r'   | |   | (__       | |   | |   | || (__        | |      | (___) || (___) || |      | |      | (__    |   \ | || |      | (__     \n'
r'   | |   |  __)      | |   | |   | ||  __)       | |      |  ___  ||  ___  || |      | |      |  __)   | (\ \) || | ____ |  __)    \n'
r'   | |   | (         | |   | |   | || (          | |      | (   ) || (   ) || |      | |      | (      | | \   || | \_  )| (       \n'
r'   | |   | (____/\   | |   | (___) || (____/\    | (____/\| )   ( || )   ( || (____/\| (____/\| (____/\| )  \  || (___) || (____/\ \n'
r'   )_(   (_______/   )_(   (_______)(_______/    (_______/|/     \||/     \|(_______/(_______/(_______/|/    )_)(_______)(_______/ '
)

cloudString1 = (  
r"    ____ _  \n"
r"  _(    `.) \n"
r" ( (    ) ))\n"
r"( (   )  _) \n"
r" '.__)--'   "
)
cloudString2 = (
r"  _ __   \n"
r" ( (  )`.\n"
r"( (    ))\n"
r" `-(__.' "
)
 

cloudString3 = (
r" .-.. \n"
r"(_)_))  "
)


BackGroundLayer = 0
EastereggLayer = 1

ShadowLayer = 2
IslandLayer = 3
CloudLayer = 10
AirplaneLayer = 15
CrosshairLayer = 20
ExplosionLayer = 30

COLOR_WATER = 1
COLOR_CLOUD = 2
COLOR_SHADOW = 3
COLOR_BROWN = 4
COLOR_FRAME = 5
COLOR_CROSSHAIR = 6
COLOR_AIRPLANE = 7
COLOR_EXPLOSION = 8

###################################################
def parseTxtToPoints(parseString, Color, opaque, removeChar = ''):
    x = -1
    y = 0
    points = []
    for i in range( len(parseString)):
        c = parseString[i]
        x = x + 1
        if (c != " ") | (opaque == True):
            if (c == "n") & (parseString[i-1] == '\\'):
                x = -1
                y = y + 1
            else:
                if c == "\\":
                    if i < (len(parseString)):
                        if (c == "\\") & (parseString[i+1] == 'n'):
                            continue
                        else:
                            points.append(GraphicsPoint(x, y, c , Color ))
                else:
                        points.append(GraphicsPoint(x, y, c , Color ))
    retpoints = []
    if removeChar != '':
        for point in points:
            if point.C != removeChar:
                retpoints.append(point)
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

    def __eq__(self, other):
        if isinstance(other, GraphicsPoint):
            return (self.X == other.X) and ( self.Y == other.Y)
        return False
   
###################################################
class DrawableObject():
    def __init__(self, Layer, objString, X, Y, color, opaque = False):

        self.x_offset = X
        self.y_offset = Y
        self.layer = Layer
        self.Color = color
        self.points = parseTxtToPoints(objString, color,opaque)
        # find max
        self.width  = 0
        self.height  = 0
        for p in self.points:
            if p.X > self.width:
                self.width = p.X
            if p.Y > self.height:
                self.height = p.Y


    def get(self):
        returnPoints = []
        for p in self.points:
            returnPoints.append(GraphicsPoint((p.X + self.x_offset),(p.Y + self.y_offset), p.C, p.Color))
        return returnPoints  

    def placeAt(self, X , Y):
        
        self.x_offset = X
        self.y_offset = Y

    def getChilds(self):
        return []


###################################################
class Frame(DrawableObject):
    def __init__(self, X, Y, C):
        self.points = []
        self.layer = 100
        for y in range(Y):
            for x in range(X):
                if y == 0:
                    self.points.append(GraphicsPoint(x,y,C,COLOR_FRAME))
                else:
                    if y == (Y-1):
                        self.points.append(GraphicsPoint(x,y,C,COLOR_FRAME))
                    else:
                        if (x == 0) | (x == X-1):
                            self.points.append(GraphicsPoint(x,y,C,COLOR_FRAME))
    def get(self):
        return self.points



###################################################
class MoveAbleObject(DrawableObject):
    def __init__(self, Layer, objString, X , Y, Color, Direction, Speed, opaque = True):
        super().__init__(Layer, objString, X , Y, Color, opaque)
        self.speed = Speed
        self.direction = Direction
       
    def move(self):
        if self.direction == "left":
            self.x_offset = self.x_offset - self.speed
        else:
            if self.direction == "right":
                self.x_offset = self.x_offset + self.speed

    def get(self):
        return super().get()

###################################################
class Background():

    def __init__(self):
        self.cnt = 0
        self.UpdateMultiplikator = 4
        self.Background()
        self.layer = 0

    def Background(self):
        background = []
        x = 0
        y = 0
        while(True):
            segment = Water().get()
            segment.placeAt(x,y)
            background.extend(segment.get())
            x += segment.width
            if x > curses.COLS and y <= curses.LINES:
                x = 0
                y += 1
            if x > curses.COLS and y > curses.LINES:
                self.oldBackground = background
                return background


    def get(self):
        if self.cnt < self.UpdateMultiplikator:
            self.cnt += 1
            return self.oldBackground
        else:
            self.cnt = 0
            retval = self.Background()
            return retval 

    # lazy workaround, should inherit from drawable object instead
    def getChilds(self):
        return []

###################################################

class Easterhenn(DrawableObject):
    def __init__(self):
        super().__init__(EastereggLayer, chickenString, -100, -100, COLOR_WATER , False)
        self.cnt = 0
        self.old = []

    def get(self):
        retval = []
        if self.cnt < 5:
            self.cnt += 1
        if self.cnt == 5:
            self.cnt += 1
            newX = random.randrange(0, curses.COLS, 1)
            newY = random.randrange(self.height, curses.LINES, 1)
            self.placeAt(newX, newY)
            retval = super().get()
        if (self.cnt > 5) & (self.cnt < 10):
            self.cnt += 1
            retval = super().get()
        if self.cnt == 10:
            self.cnt = 0
        return retval

###################################################

class Crosshair(DrawableObject):
    def __init__(self):
        crosshairString = (
r"<+> \n"
r" V  \n"
)

        super().__init__(CrosshairLayer,crosshairString,int( curses.COLS/2),int(curses.LINES / 2),COLOR_CROSSHAIR)

    def getTarget(self):
        return [self.x_offset +1, self.y_offset]

###################################################
class Water:
    def __init__(self):
        C = COLOR_WATER
        waterSegments = []
        X = 0
        Y = 0
        waterSegments.append(DrawableObject(BackGroundLayer, ' _=_=-=', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' ==-', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' =-', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' -=.--', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' _=-=-', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' -_=-=_', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' =-=-_-__=_-=', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' _=_=-=_', X, Y, C, True))
        waterSegments.append(DrawableObject(BackGroundLayer, ' _             _', X, Y, C, True))
        # return a random water segment from the set
        self.segment = waterSegments[random.randrange(0, len(waterSegments), 1)]

    def get(self):
        return self.segment
   
###################################################

class Screen:
    layers = []
    for _ in range(150):
        layers.append([])
       
    drawables = []

    size = os.get_terminal_size()
    cursesScreen = curses.initscr()
    cursesScreen = curses.newwin(curses.LINES -1 ,curses.COLS -1)
    cursesScreen.keypad(0)
   
    def addDrawable(obj):
        Screen.layers[obj.layer].append(obj)
        for child in obj.getChilds():
            Screen.layers[obj.layer].append(child)

    def removeDrawable(obj):
        if obj in Screen.layers[obj.layer]:
            Screen.layers[obj.layer].remove(obj)
        for child in obj.getChilds():
            if obj in Screen.layers[obj.layer]:
                Screen.layers[obj.layer].remove(child)


    def draw():
        Screen.cursesScreen.erase()
        layers = Screen.layers.copy()
        for i in range(len(layers)):
            if layers[i] == []:
                continue
            for drawable in layers[i]:
                try:
                    drawable.move()
                except:
                    pass

        layers = Screen.layers.copy()
        for i in range(len(layers)):
            if layers[i] == []:
                continue
            for drawable in layers[i]:
                for p in drawable.get():
                    if p.X < curses.COLS -2 and p.X >= 0 and p.Y < curses.LINES - 1 and p.Y >= 0:
                        Screen.cursesScreen.addstr(p.Y, p.X, p.C,curses.color_pair(p.Color))
        Screen.cursesScreen.refresh()


##################################################
class Cloud(MoveAbleObject):

    def __init__(self, X, Y, Direction):
        self.id = random.randrange(1,100,1)
        cloudsStrings = []
        cloudsStrings.append(cloudString1)
        cloudsStrings.append(cloudString2)
        cloudsStrings.append(cloudString3)
        cloudString = cloudsStrings[random.randrange(0, len(cloudsStrings), 1)]

        super().__init__( CloudLayer, cloudString, X, Y, COLOR_CLOUD, Direction, 3, True)

        # construct a shadow for the cloud
        self.shadow = MoveAbleObject( ShadowLayer, cloudString, X-3,Y + self.height + 3, COLOR_SHADOW , Direction, 3, False)

    def __del__(self):
        del self.shadow

    def getChilds(self):
        l = []
        l.append(self.shadow)
        return l
###################################################

class Explosion(DrawableObject):
    def __init__(self, X, Y):
        explosionString1 = (
  r" .---. \n"
  r" (\|/)   "
)
    
        explosionString2 = (
  r" '.\|/.' \n"
  r" (\   /)   "
)
        self.layer = ExplosionLayer
        self.frame1 = DrawableObject(ExplosionLayer, explosionString1,X-3,Y-1, COLOR_EXPLOSION, False)
        self.frame2 = DrawableObject(ExplosionLayer, explosionString2,X-4,Y-1, COLOR_EXPLOSION, False)
        self.cnt = 0
        self.fnr = 1

    def get(self):
        if self.cnt == 4:
            Screen.removeDrawable(self)
        if self.fnr == 1:
            self.fnr = 2
            self.cnt += 1 
            return self.frame1.get()
        if self.fnr == 2:
            self.fnr = 1
            self.cnt += 1 
            return self.frame2.get()     

###################################################
class Bomb(MoveAbleObject):
    def __init__(self,Layer, X, Y, Color, Direction, Speed, XTarget, YTarget):
        bombString = r">-> \n"
        super().__init__(Layer, bombString, X, Y, Color, Direction, Speed, False)
        self.xTarget = XTarget
        self.yTarget = YTarget
        self.bombExploded = False
        self.started = False

    def  checkExplosion(self):
        if (self.x_offset + 2 >= self.xTarget) & (self.y_offset == self.yTarget):
            self.bombExploded = True
            explosion = Explosion(self.xTarget, self.yTarget)
            Screen.addDrawable(explosion)
            Screen.removeDrawable(self)
            return True
        else:
            return False

    def setOff(self):
        self.started = True
    
    def move(self):
        if self.started == True:
            
            xdist = self.xTarget - self.x_offset + 2# + because rocket extends to the right, and the tip arrives first
            if (xdist > 0) & (xdist > self.speed):
                self.x_offset += self.speed
            else:
                if (xdist > 0) & (xdist <= self.speed):
                    self.x_offset += 1
            if (self.y_offset < self.yTarget):
                self.y_offset += 1
            self.checkExplosion()
        else:
            super().move()

###################################################
class AirPlane(MoveAbleObject):
    def __init__(self, X, Y, tX,tY):
        self.target_x = tX
        self.target_y = tY
        self.flightHeight = Y
        self.bombExploded = False
        planeString = (
r" (\__.-. | \n"
r" == ===_]+ \n"
r"   //    | \n"
    )
        super().__init__(AirplaneLayer, planeString, X , tY - Y, COLOR_AIRPLANE, "right", 3, False )
        self.bomb = Bomb(AirplaneLayer,X+2,tY-Y+1,COLOR_AIRPLANE,"right",3,tX,tY)


    def getChilds(self):
        l = []
        l.append(self.bomb)
        return l

    def get(self):
        if self.bombExploded == False:
            self.bombExploded = self.bomb.bombExploded
        else:
            self.y_offset -= 1
        if (self.bombExploded == False) & (self.x_offset >= (self.target_x - 20)):
                self.bomb.setOff()
        if (self.y_offset < -5) | (self.x_offset > curses.COLS + 5):
            Screen.removeDrawable(self)
        return super().get()

###################################################
class Game:

    def __init__(self):
        self.updateIntervall = 0.25
        self.cnt = 0
        self.endGame = False
 
        curses.initscr()  
        curses.start_color()
        curses.curs_set(False)
        curses.noecho()

        curses.init_pair(COLOR_WATER, 27, 33) # lightBlue/Blue for water
        curses.init_pair(COLOR_CLOUD, 253, 33) # white on blue for clouds
        curses.init_pair(COLOR_SHADOW, 233,33) #gray on blue for cloudshadow
        curses.init_pair(COLOR_BROWN, 196, 33) #
        curses.init_pair(COLOR_FRAME, 221, 33) #
        curses.init_pair(COLOR_CROSSHAIR, 1, 33) #
        curses.init_pair(COLOR_AIRPLANE, 7, 33) #
        curses.init_pair(COLOR_EXPLOSION, 13, 33) #

        self.keyctl = KeyboardController()
         
        self.crosshair = Crosshair()
        Screen.addDrawable(self.crosshair)

        Screen.addDrawable(Frame(curses.COLS-2,curses.LINES-1,'#'))
        Screen.addDrawable(Easterhenn())

        locale.setlocale(locale.LC_ALL,"")
        self.background = Background()
        Screen.addDrawable(self.background)

        #Create self moving clouds and place them initially out of sight
        self.clouds = []

        for _ in range(4):
            cloud1 = Cloud(-100, -100, "left")
            self.clouds.append(cloud1)
            Screen.addDrawable(cloud1)

    def gameLoop(self):
        time.sleep(self.updateIntervall)
        self.keyControLogic()
        self.logicLoop()
        self.graphicsLoop()
   
    def logicLoop(self):
        self.cloudLogic()

    def cloudLogic(self):
        # create new clouds after old ones have left the screen
        for i in range(len(self.clouds)):
            cloud = self.clouds[i]
            if cloud.x_offset <= -10:
                newX = curses.COLS + random.randrange(0, curses.COLS, 1)
                newY = random.randrange(0, curses.LINES - ( 2 * cloud.height) - 4, 1)
                Screen.removeDrawable(cloud)
                newCloud = Cloud(newX, newY, "left")
                Screen.addDrawable(newCloud)
                self.clouds[i] = newCloud
                self.airplane = ""

    def keyControLogic(self):
        if self.keyctl.getKeyPressed():
            key = self.keyctl.getKey()
            if key == curses.KEY_LEFT:
                self.crosshair.placeAt(self.crosshair.x_offset - 1, self.crosshair.y_offset)
            if key == curses.KEY_RIGHT:
                self.crosshair.placeAt(self.crosshair.x_offset + 1, self.crosshair.y_offset)
            if key == curses.KEY_UP:
                self.crosshair.placeAt(self.crosshair.x_offset, self.crosshair.y_offset - 1 )
            if key == curses.KEY_DOWN:
                self.crosshair.placeAt(self.crosshair.x_offset, self.crosshair.y_offset + 1)
            if key == 27:#Escape
                self.endGame = True
            if key == 32:#Space
                self.airplane = AirPlane(-5, 5, self.crosshair.getTarget()[0], self.crosshair.getTarget()[1])
                Screen.addDrawable(self.airplane)

    def graphicsLoop(self):
        Screen.draw()

def Main(scr):
    game = Game()

    while True:
            game.gameLoop()
            if game.endGame  == True:
                break
    endCurses()
    sys.exit(0)


if __name__ == "__main__":
    cursesWrapper(Main)

