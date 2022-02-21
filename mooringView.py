import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from draggableWidget import *
from dropZone import DropZone

class MooringView(QWidget):
    '''class managing the left window diplaying mooring element using draggable elements'''

    def __init__(self,facade):
        '''initialisation of variable and layout
            sucribing to facade as an observer'''
        super(MooringView, self).__init__()
        self.facade = facade
        self.facade.subscribe(self)
        self.mooringLayout = QVBoxLayout(self)
        #self.resize(400, 1000)
        self.mooringLayout.setSpacing(0)
        self.mooringLayout.setContentsMargins(0,0,0,0)
        self.update()

    def update(self):
        '''use when notify, get access to mooring information and display'''
        mooringList = list()
        mooringList = self.facade.getMooring()
        self.clear()
        id = 0
        dropZone = DropZone(self.facade,id)
        self.mooringLayout.addWidget(dropZone)
        for i in mooringList:
            elementWidget = DraggableWidget(i.name,i.image)
            self.mooringLayout.addWidget(elementWidget)
            id =id+1
            dropZone = DropZone(self.facade,id)
            self.mooringLayout.addWidget(dropZone)

    def clear(self):
        '''clear the layout of all the widget'''
        for i in reversed(range(self.mooringLayout.count())): 
            widgetToRemove = self.mooringLayout.itemAt(i).widget()
            # remove it from the layout list
            self.mooringLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.layout().deleteLater()