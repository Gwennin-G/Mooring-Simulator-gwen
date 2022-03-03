from abc import ABC, abstractmethod

from mooring.link import Link

class Element(ABC): # hériter de ABC(Abstract base class)

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.__before__ = None  #an element have none or one link to a previous element
        self.__after__ = []     #an element have none or multiple links to next elements 

    #getter to an element parameters 
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def category(self):
        pass

    @property
    @abstractmethod
    def imageFile(self):
        pass

    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    @abstractmethod
    def length(self):
        pass


    @property
    @abstractmethod
    def projectedArea(self):
        pass

    @property
    @abstractmethod
    def normalDragCoeff(self):
        pass

    @property
    @abstractmethod
    def tangentialDragCoeff(self):
        pass

    #getter/setter for Link
    @property
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


    