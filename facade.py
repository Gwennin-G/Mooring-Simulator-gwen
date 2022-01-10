import sys

from mainView import *

class Facade():
    '''add documentation here'''

    def __init__(self):
        '''add documentation here'''
        self.mooringList = list()
        self.libraryList= list()
        self.libraryList.append(libraryElement("Benthos","ressources\\pictures\\1Benthos_1m_chaine.bmp") )
        self.libraryList.append(libraryElement("cable","ressources\\pictures\\cable.bmp") )
        self.libraryList.append(libraryElement("chaine","ressources\\pictures\\chaine.bmp") )
        self.libraryList.append(libraryElement("lest","ressources\\pictures\\lest.bmp") )
       
    def getLibrary(self):
        return self.libraryList


class libraryElement():
    '''add documentation here'''
    
    def __init__(self,name,image):
        self._name = name
        self._image = image

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image
