import sys, random

from functools import partial

from PyQt5.Qt import *

from plugins import Nodes

class MainWindow(QMainWindow):

    numberOfNodesSquared = 2
    nodesGrid = []
    didWin = False

    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QVBoxLayout(centralWidget)

        self.setup()
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet("background-color: black")
        self.setWindowTitle("Lights Out")

    def nodePress(self, row, col):
        self.nodesGrid[row][col].updateState()
        self.updateNeighbors(row, col)
        self.getWin()
        if (self.didWin):
            self.win()

    def setup(self):
        self.didWin = False
        self.clearScreen()
        self.nodesGrid = []

        for row in range(self.numberOfNodesSquared):
            grid = []
            for col in range(self.numberOfNodesSquared):

                button = Nodes.Nodes()
                button.setState()

                grid.insert(col, button)
                button.clicked.connect(partial(self.nodePress, row, col))
                self.layout.addWidget(button, row+1, col)

            self.nodesGrid.insert(row, grid)

    def updateNeighbors(self, row, col):
        up = down = right = left = True 
        if (row == 0):
            up = False
        if (col == 0):
            left = False
        if (row == self.numberOfNodesSquared-1):
            down = False
        if (col == self.numberOfNodesSquared-1):
            right = False

        if up:
            self.nodesGrid[row-1][col].updateState()
        if down:
            self.nodesGrid[row+1][col].updateState()
        if left:
            self.nodesGrid[row][col-1].updateState()
        if right:
            self.nodesGrid[row][col+1].updateState()

    def getWin(self):
        total = 0
        for ar in self.nodesGrid:
            for node in ar:
                total += node.state

        if (total == self.numberOfNodesSquared**2):
            self.didWin = True

    def win(self):  
        self.clearScreen()

        label = QLabel("You win!")
        replayButton = QPushButton(self)

        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)
        self.layout.addWidget(replayButton)
        
        replayButton.clicked.connect(partial(self.setup))

    def clearScreen(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
