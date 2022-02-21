import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DropZone(QWidget):
    def __init__(self,facade,id):
        super().__init__()
        self.facade = facade
        self.id = id
        self.setAcceptDrops(True)
        layout = QHBoxLayout(self)
        label = QLabel("")
        layout.addWidget(label)
        label.setStyleSheet("""
            background-color: red;
        """)

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
            self.facade.addMooringElement(event.mimeData().text(),self.id)
            