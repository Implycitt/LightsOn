import sys
from PyQt5.Qt import *

from plugins import Nodes, Window

def createWindow():
    app = QApplication(sys.argv)
    window = Window.MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    createWindow()
