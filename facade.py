import sys

from mainView import *

class Facade():
    '''Temporary facade class  use to test views'''

    def __init__(self):
        '''initialisation of a library and a mooring model'''
        self.observableList = list()
        self.mooringList = list()
        self.libraryList= list()
        self.libraryList.append(libraryElement("Benthos","ressources\\pictures\\1Benthos_1m_chaine.bmp") )
        self.libraryList.append(libraryElement("cable","ressources\\pictures\\cable.bmp") )
        self.libraryList.append(libraryElement("chaine","ressources\\pictures\\chaine.bmp") )
        self.libraryList.append(libraryElement("lest","ressources\\pictures\\lest.bmp") )
       
    def getLibrary(self):
        return self.libraryList

    def getEntityByName(self,name):
        for entity in self.libraryList:
            if entity.name == name:
                return entity
        return None
    
    def getMooring(self):
        return self.mooringList

    def addMooringElement(self,name,indexPosition):
        element = self.getEntityByName(name)
        self.mooringList.insert(indexPosition,element)
        self.notice()

    def subscribe(self,observable):
        self.observableList.append(observable)

    def notice(self):
        for o in self.observableList:
            o.update()

class libraryElement():
    '''elements representation needed by the view'''
    
    def __init__(self,name,image):
        self._name = name
        self._image = image

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image
