import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from draggableWidget import *

class MooringView(QWidget):
    def __init__(self,facade):
        super(MooringView, self).__init__()
        self.facade = facade
        self.mooringLayout = QVBoxLayout(self)
        self.resize(400, 201)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        if event.mimeData().hasImage() & event.mimeData().hasText():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
            
    def dropEvent(self,event):
        if event.mimeData().hasImage() & event.mimeData().hasText():
            droppedWidget = DraggableWidget(event.mimeData().text(),event.mimeData().imageData())
            self.mooringLayout.addWidget(droppedWidget)