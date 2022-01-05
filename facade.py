import sys

from mainView import *

class Facade():
    def __init__(self):
        self.mooringList = list()
        self.libraryList= list()
        self.libraryList.append(libraryElement("Benthos","viewTest\\ressources\\pictures\\1Benthos_1m_chaine.bmp") )
        self.libraryList.append(libraryElement("cable","viewTest\\ressources\\pictures\\cable.bmp") )
        self.libraryList.append(libraryElement("chaine","viewTest\\ressources\\pictures\\chaine.bmp") )
        self.libraryList.append(libraryElement("lest","viewTest\\ressources\\pictures\\lest.bmp") )
       
    def getLibrary(self):
        return self.libraryList


class libraryElement():
    def __init__(self,name,image):
        self.name = name
        self.image = image

    def getName(self):
        return self.name

    def getImage(self):
        return self.image
