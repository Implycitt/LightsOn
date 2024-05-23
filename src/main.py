import sys, random

from functools import partial

from PyQt5.Qt import *

class MainWindow(QMainWindow):
    
    numberOfNodesSquared = 3
    nodesGrid = []
    
    def __init__(self):
        super().__init__()
        self.setUI()

    def buttonPress(self, row, col):
        self.nodesGrid[row][col].setText("Pressed")

    def setUI(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.layout = QGridLayout(centralWidget)

        for row in range(self.numberOfNodesSquared):
            grid = []
            for col in range(self.numberOfNodesSquared):

                buttonState = random.randint(0, 1);
                button = QPushButton(f"{buttonState}")

                grid.insert(col, button)
                button.clicked.connect(partial(self.buttonPress, row, col))
                self.layout.addWidget(button, row+1, col)

            self.nodesGrid.insert(row, grid)

        self.setFixedSize(QSize(800, 600))
        self.setWindowTitle("Lights Out")

def window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
