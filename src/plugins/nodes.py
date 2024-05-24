from PyQt5.Qt import *

from random import randint

class Nodes(QPushButton):

    state = 0 
    numberPresses = 0

    def __init__(self):
        super().__init__()
        self.setState()

    def setState(self):
        self.state = randint(0, 1)
        self.presses = self.state

    def updateState(self):
        self.presses += 1
        self.state = (self.presses % 2)
        self.setText(f"{self.state}")
    
