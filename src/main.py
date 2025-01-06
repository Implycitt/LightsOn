import sys, numpy
from PyQt5.Qt import *
from fractions import Fraction

from plugins import Nodes, Window, Solve

def createWindow():
    app = QApplication(sys.argv)
    window = Window.MainWindow()
    window.show()
    sys.exit(app.exec_())


def main():
    createWindow()

if __name__ == "__main__":
	main()
