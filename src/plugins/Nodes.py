from PyQt5.Qt import *

from random import randint

class Nodes(QPushButton):

    state = 0 
    numberPresses = 0
    position = 0
    row = 0
    col = 0

    def __init__(self):
        super().__init__()
        self.setMinimumSize(100, 100)
        self.setMaximumSize(100, 100)
        self.setState()
        self.changeColor()

    def setPosition(self, pos):
        self.position = pos

    def setRow(self, row):
        self.row = row

    def setCol(self, col):
        self.col = col 

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def setState(self):
        self.state = randint(0, 1)
        self.presses = self.state

    def updateState(self):
        self.presses += 1
        self.state = (self.presses % 2)
        self.changeColor()
        self.updateClicks()

    def changeColor(self):
        self.resize(150, 150)
        if (self.state == 1):
            self.setStyleSheet("background-color: green; border: 2px solid white")
        else:
            self.setStyleSheet("background-color: red; border: 2px solid white")

    def updateClicks(self):
        self.numberPresses += 1

    def getClicks(self):
        return self.numberPresses
