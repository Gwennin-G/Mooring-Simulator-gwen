import sys

from mainView import *

class Facade():
    '''Temporary facade class  use to test views'''
    '''Facade provide communication between Views and Mooring or Librairy intern representation'''

    def __init__(self):
        '''initialisation of a library and a mooring model'''
        self.observerList = list()
        self.mooringList = list()
        self.libraryList= list()
        self.libraryList.append(libraryElement("Benthos","ressources\\pictures\\1Benthos_1m_chaine.bmp") )
        self.libraryList.append(libraryElement("cable","ressources\\pictures\\cable.bmp") )
        self.libraryList.append(libraryElement("chaine","ressources\\pictures\\chaine.bmp") )
        self.libraryList.append(libraryElement("lest","ressources\\pictures\\lest.bmp") )
       
    def getLibrary(self):
        '''return util information for grafic library view'''
        return self.libraryList

    def getEntityByName(self,name):
        '''return information for grafic view of a library entity '''
        for entity in self.libraryList:
            if entity.name == name:
                return entity
        return None
    
    def getMooring(self):
        '''return util information for Mooring display'''
        return self.mooringList

    def addMooringElement(self,name,indexPosition):
        '''return util information for grafic library view'''
        element = self.getEntityByName(name)
        self.mooringList.insert(indexPosition,element)
        self.notice()

    def subscribe(self,observer):
        '''sucribing a observer to Facade'''
        self.observerList.append(observer)

    def notice(self):
        '''notice all the observer'''
        for o in self.observerList:
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
