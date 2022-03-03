from abc import ABC, abstractmethod
from mooring.element import Element

class Factory(ABC): # hériter de ABC(Abstract base class)
    
    @abstractmethod
    def __init__(self, category ,name ,imageFile ):
        super().__init__()
        self.__category = category
        self.__name = name
        self.__imageFile=imageFile

    @abstractmethod
    def creationElement(self) -> Element:
        pass

    @property
    def category(self):
        return self.__category

    @property
    def name(self):
        return self.__name

    @property
    def imageFile(self):
        return self.__imageFile

        