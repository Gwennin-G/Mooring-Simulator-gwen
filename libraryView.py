import sys 

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from draggableWidget import *
from facadeTest import *

class LibraryView(QWidget):
    '''class managing the right window diplaying library element using draggable elements'''

    def __init__(self,facade):
        '''initialisation of variable and layout,
            acess to library grafic representation information 
            sucribing to facade as an observer'''
        super(LibraryView, self).__init__()
        self.facade = facade
        self.facade.subscribe(self)
        self.layout = QGridLayout(self)
        self.__getLibrary()
        self.setLayout(self.layout)
        self.resize(400, 201)

    def __getLibrary(self):
        '''get acess to util information to grafic representation and addition to the layout'''
        libraryList = list()
        libraryList = self.facade.getLibrary()
        for i in libraryList:
            elementWidget = DraggableWidget(i.name, i.image)
            self.layout.addWidget(elementWidget)
    
    def update(self):
        '''not use for the moment'''
        None

if __name__ == '__main__':
    print("test")
    app = QApplication(sys.argv)
    facade = Facade()
    window = LibraryView(facade)
    window.setGeometry(600, 100, 200, 30)
    window.show()
    sys.exit(app.exec_())
    