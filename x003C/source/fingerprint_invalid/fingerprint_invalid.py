import random
import time

from rich.live import Live
#from rich.table import Table
from rich.console import Console

import os
   
###################################################
def draw():
    screen.draw()
###################################################

class Screen:
    
    

    def __init__(self):
        self.toggle = 1
      
    def toggleScreen(self):
        size = os.get_terminal_size()
        self.lines = [] 
        if self.toggle is 1:
            c = '-'
            self.toggle = 0
        else:
            c = '+'
            self.toggle = 1
        for _ in range(size.lines):
            line = [c] * (size.columns - 1)
            self.lines.append(line)

    def draw(self):
        console.clear_live()
        self.toggleScreen()
        for line in self.lines:
            line = '[blue]' + ''.join(line)
            console.print(line)

###################################################
console = Console(force_terminal=True)
screen = Screen()
#screen.draw()

with Live(draw(), refresh_per_second=4) as live:
    while True:
        #time.sleep(0.4)
        live.update(draw())