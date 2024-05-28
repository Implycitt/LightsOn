import sys, random

from functools import partial

from PyQt5.Qt import *

from plugins import Nodes, solve

class MainWindow(QMainWindow):

    numberOfNodesSquared = 4
    nodesGrid = []
    solveMatrix = []
    didWin = False

    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QGridLayout(centralWidget)
        self.layout.setSpacing(0)

        self.setup()
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet("background-color: slategrey")
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
        self.solveMatrix = []

        i = 0
        for row in range(self.numberOfNodesSquared):
            grid = []
            for col in range(self.numberOfNodesSquared):

                button = Nodes.Nodes()
                state = button.state

                grid.insert(col, button)
                self.solveMatrix.insert(i, state)

                button.clicked.connect(partial(self.nodePress, row, col))
                self.layout.addWidget(button, row+1, col)
                i += 1

            self.nodesGrid.insert(row, grid)
        self.startSolve()

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

        replayButton = QPushButton(self)
        replayButton.setText("Play Again")
        replayButton.setStyleSheet("background-color: white")
        replayButton.setMinimumSize(300, 50)
        replayButton.setMaximumSize(300, 50)

        label = QLabel("You win!")
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color: white")
        label.setMinimumSize(300, 50)
        label.setMaximumSize(300, 50)

        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label, 0, 0)
        self.layout.addWidget(replayButton, 1, 0)
        
        replayButton.clicked.connect(partial(self.setup))

    def startSolve(self):
        s = solve.Solve()
        s.setStartMatrix(self.solveMatrix)
        s.setSize(self.numberOfNodesSquared)
        s.getTransformations()
        
    def clearScreen(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)
