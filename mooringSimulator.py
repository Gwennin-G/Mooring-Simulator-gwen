'''Launcher of Mooring Simulator'''

import sys

from mainView import *
from facade import *
from PyQt5.QtCore import *

'''add usage here'''
app = QApplication(sys.argv)
facade = Facade()
mainWindow = MainView(facade)
mainWindow.showView()
app.exec()
