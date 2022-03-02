from abc import ABC, abstractmethod

from mooring.link import Link

class Element(ABC): # hériter de ABC(Abstract base class)

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__before__ = None  #an element have none or one link to a previous element
        self.__after__ = []     #an element have none or multiple links to next elements 

    #getter to an element parameters 
    @abstractmethod
    @property
    def name(self):
        pass

    @abstractmethod
    @property
    def category(self):
        pass

    @abstractmethod
    @property
    def imageFile(self):
        pass

    @abstractmethod
    @property
    def mass(self):
        pass

    @abstractmethod
    @property
    def length(self):
        pass

    @abstractmethod
    @property
    def diameter(self):
        pass

    @abstractmethod
    @property
    def projectedArea(self):
        pass

    @abstractmethod
    @property
    def normalDragCoef(self):
        pass

    @abstractmethod
    @property
    def tangentialCoef(self):
        pass

    #getter/setter for Link
    @property
    def before(self):
        return self.__before__

    @property.setter
    def before(self):
        return self.__before__
    
    @before.setter
    def before(self, newElement) :
        self.__before__ = newElement

    @property
    def after(self):
        return self.__after__

    def addAfter(self, newElement) :
        self.__after__.append(newElement)
    
    def removeAfter(self, removedElement) :
        if self.__after__.count(removedElement)>0:
            self.__after__.remove(removedElement)


    