from mooring.unmodifiableElement import UnmodifiableElement
from factory import Factory

class UnmodifiableElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,mass,length,projectedArea,normalArea,normalDragCoeff,tangentialDragCoeff):
        super().__init__(categorie,name,imageFile)
        self.__mass__ = mass
        self.__length__ = length
        self.__projectedArea__ = projectedArea
        self.__normalArea__ = normalArea
        self.__normalDragCoeff__ = normalDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff

    def creationElement(self) -> UnmodifiableElement:
        return UnmodifiableElement(self)

    @property
    def mass(self):
        return self.__mass__

    @property
    def length(self):
        return self.__length__

    @property
    def projectedArea(self):
        return self.__projectedArea__

    @property
    def normalArea(self):
        return self.__normalArea__

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff__

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff__
