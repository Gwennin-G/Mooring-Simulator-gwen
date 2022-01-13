import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from libraryView import *
from mooringView import *
from facade import *

class MainView(QMainWindow):
    '''Manage other View and general action'''

    def __init__(self,facade):
        '''creation of mooringView and libraryView for display'''
        super(MainView, self).__init__()
        self.facade = facade
        self.mooringView = MooringView(facade)
        self.mooringDockWidget = QDockWidget()
        self.mooringDockWidget.setWidget(self.mooringView)
        self.addDockWidget(Qt.LeftDockWidgetArea,
                           self.mooringDockWidget)
        self.libraryView = LibraryView(facade)
        self.libraryDockWidget = QDockWidget()
        self.libraryDockWidget.setWidget(self.libraryView)
        self.addDockWidget(Qt.RightDockWidgetArea,
                           self.libraryDockWidget)

    def showView(self):
        self.show()

if __name__ == '__main__':
    print("test")
    app = QApplication(sys.argv)
    facade = Facade()
    window = MainView(facade)
    window.showView()

    app.exec()