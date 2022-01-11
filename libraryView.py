import sys 

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from draggableWidget import *
from facade import *

class LibraryView(QWidget):
    '''class managing the bottom window containing draggable elements'''

    def __init__(self,facade):
        '''add documentation here'''
        super(LibraryView, self).__init__()
        self.facade = facade
        self.facade.subscribe(self)
        self.layout = QGridLayout(self)

        '''elementWidget1 = DraggableWidget("element : 1",'dragAndDrop\\aquadopp.bmp')
        elementWidget2 = DraggableWidget("element : 2",'dragAndDrop\\aquadopp.bmp')
        #elementWidget.setAlignment(Qt.AlignRight)
        self.layout.addWidget(elementWidget1)
        self.layout.addWidget(elementWidget2)'''

        self.__getLibrary()
        self.setLayout(self.layout)
        self.resize(400, 201)

    def __getLibrary(self):
        '''add documentation here'''
        libraryList = list()
        libraryList = self.facade.getLibrary()
        for i in libraryList:
            elementWidget = DraggableWidget(i.name, i.image)
            self.layout.addWidget(elementWidget)
    
    def update(self):
        None

if __name__ == '__main__':
    print("test")
    app = QApplication(sys.argv)
    facade = Facade()
    window = LibraryView(facade)
    window.setGeometry(600, 100, 200, 30)
    window.show()
    sys.exit(app.exec_())
    