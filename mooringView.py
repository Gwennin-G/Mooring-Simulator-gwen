import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from draggableWidget import *

class MooringView(QWidget):
    '''add documentation here'''

    def __init__(self,facade):
        '''add documentation here'''
        self.elementList = list()
        super(MooringView, self).__init__()
        self.facade = facade
        self.facade.subscribe(self)
        self.mooringLayout = QVBoxLayout(self)
        self.resize(400, 201)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        '''add documentation here'''
        if event.mimeData().hasImage() & event.mimeData().hasText():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
            
    def dropEvent(self,event):
        '''add documentation here'''
        if event.mimeData().hasImage() & event.mimeData().hasText():
            self.facade.addMooringElement(event.mimeData().text(),0)
            self.dropListLocation(0)

    def update(self):
        '''add documentation here'''
        mooringList = list()
        mooringList = self.facade.getMooring()
        self.clear()
        for i in mooringList:
            elementWidget = DraggableWidget(i.name,i.image)
            self.elementList.append(elementWidget)
            self.mooringLayout.addWidget(elementWidget)

    def clear(self):
        for i in reversed(range(self.mooringLayout.count())): 
            widgetToRemove = self.mooringLayout.itemAt(i).widget()
            # remove it from the layout list
            self.mooringLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            self.elementList.clear()
            widgetToRemove.layout().deleteLater()

    def dropListLocation(self,yPosition):
        
        for i in range(self.mooringLayout.count()):
            child = self.mooringLayout.itemAt(i)
            print('element')
            print(i)
            print(child.widget().parent().parent().geometry())
            print(child.widget().parent().geometry())
            print(child.widget().geometry())
            print(child.widget().layout().geometry())
        '''print(len(self.elementList))
        for i in range(len(self.elementList)):
            child = self.elementList[i]
            print('element')
            print(i)
            print(child.parent().parent())
            print(child.parent())
            print(child)
            print(child.layout())'''