import sys, random, math, numpy

from functools import partial

from PyQt5.Qt import *

from plugins import Nodes, Solve

class MainWindow(QMainWindow):

    numberOfNodesSquared = 3
    clicks = 0
    nodesGrid = []
    solveMatrix = []

    def __init__(self):
        super().__init__()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QGridLayout(centralWidget)

        side_layout = QGridLayout()
        solveButton = QPushButton(self)
        newButton = QPushButton(self)
        newButton.setText("new")
        solveButton.setText("Solve")
        newButton.clicked.connect(partial(self.newGame))
        solveButton.clicked.connect(partial(self.solveConfig))
        side_layout.addWidget(solveButton, 0, 0)
        side_layout.addWidget(newButton, 0, 1)

        self.layout.addLayout(side_layout, 0, 1)

        self.resize(640, 480)
        self.layout.setSpacing(0)

        self.setup()
        self.setFixedSize(QSize(800, 600))
        self.setStyleSheet("background-color: slategrey")
        self.setWindowTitle("Lights Out")

    def nodePress(self, row, col):
        self.clicks += 1
        self.nodesGrid[row][col].updateState()
        self.updateNeighbors(row, col)

    def setup(self):
        self.clicks = 0
        self.clearScreen()
        self.nodesGrid = []
        self.solveMatrix = []

        i = 0
        for row in range(self.numberOfNodesSquared):
            grid = []
            for col in range(self.numberOfNodesSquared):

                button = Nodes.Nodes()
                state = button.state
                button.setPosition(i)
                button.setCol(col)
                button.setRow(row)

                grid.insert(col, button)
                self.solveMatrix.insert(i, state)

                button.clicked.connect(partial(self.nodePress, row, col))
                self.layout.addWidget(button, row+1, col)
                i += 1

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

    def solveConfig(self):
        game = Solve.Solver(self.numberOfNodesSquared)
        config = self.getSolveMatrix()
        solution = game.solve(config)
        print("The solution of\n{}\nis\n{}".format(config, solution))
        for i in range(len(solution)):
            for j in range(len(solution[0])):
                if solution[i][j]:
                    self.nodePress(i, j)

    def clearScreen(self):
        for i in reversed(range(self.layout.count())): 
            try:
                self.layout.itemAt(i).widget().setParent(None)
            except:
                continue

    def getSolveMatrix(self):
        return numpy.array([[self.nodesGrid[j][i].state for i in range(self.numberOfNodesSquared)] for j in range(self.numberOfNodesSquared)])

    def newGame(self):
        self.clearScreen()
        self.setup()
