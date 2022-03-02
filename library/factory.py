from abc import ABC, abstractmethod
from mooring.element import Element

class Factory(ABC): # hériter de ABC(Abstract base class)
    
    @abstractmethod
    def __init__(self,category,name,imageFile):
        super().__init__()
        self.__category__ = category
        self.__name__ = name
        self.__imageFile__=imageFile

    @abstractmethod
    def creationElement(self) -> Element:
        pass

    @property
    def category(self):
        return self.__category__

    @property
    def name(self):
        return self.__name__

    @property
    def imageFile(self):
        return self.__imageFile__

        