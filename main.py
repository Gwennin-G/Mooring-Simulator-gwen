import sys

from mainView import *
from facade import *
from PyQt5.QtCore import *

app = QApplication(sys.argv)
facade = Facade()
mainWindow = MainView(facade)
mainWindow.showView()
app.exec()
