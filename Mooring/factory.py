from abc import ABC, abstractmethod
from element import Element

class Element(ABC): # hériter de ABC(Abstract base class)
    
    @abstractmethod
    def __init__(self,category,name,imageFile):
        super().__init__()
        self.__category__ = category
        self.__name__ = name
        self.__imageFile__=imageFile

    @abstractmethod
    def creationElement(self) -> Element:
        pass

    @abstractmethod
    @property
    def category(self):
        return self.__category__

    @abstractmethod
    @property
    def name(self):
        return self.__name__

    @abstractmethod
    @property
    def imageFile(self):
        return self.__imageFile__
        