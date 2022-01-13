import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from draggableWidget import *

class MooringView(QWidget):
    '''class managing the left window diplaying mooring element using draggable elements'''

    def __init__(self,facade):
        '''initialisation of variable and layout
            sucribing to facade as an observer'''
        self.elementList = list()
        super(MooringView, self).__init__()
        self.facade = facade
        self.facade.subscribe(self)
        self.mooringLayout = QVBoxLayout(self)
        self.resize(400, 201)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,event):
        '''used when a draggable element enter on the view'''
        if event.mimeData().hasImage() & event.mimeData().hasText():
            print("event accepted")
            event.accept()
        else:
            print("event rejected")
            event.ignore()
            
    def dropEvent(self,event):
        '''used when a draggable element is dropped on the view to communicate with Facade the modification of the mooring'''
        if event.mimeData().hasImage() & event.mimeData().hasText():
            self.facade.addMooringElement(event.mimeData().text(),0)
            self.dropListLocation(0)

    def update(self):
        '''use when notify, get access to mooring information and display'''
        mooringList = list()
        mooringList = self.facade.getMooring()
        self.clear()
        for i in mooringList:
            elementWidget = DraggableWidget(i.name,i.image)
            self.elementList.append(elementWidget)
            self.mooringLayout.addWidget(elementWidget)

    def clear(self):
        '''clear the layout of all the widget'''
        for i in reversed(range(self.mooringLayout.count())): 
            widgetToRemove = self.mooringLayout.itemAt(i).widget()
            # remove it from the layout list
            self.mooringLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            self.elementList.clear()
            widgetToRemove.layout().deleteLater()

    def dropListLocation(self,yPosition):
        '''Work in progress : localise the dropped element'''
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