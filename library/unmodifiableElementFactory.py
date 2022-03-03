import sys 

from library.factory import Factory
from mooring.unmodifiableElement import UnmodifiableElement



class UnmodifiableElementFactory(Factory):

    def __init__(self, categorie, name, imageFile, mass, length, projectedArea, normalDragCoeff, tangentialDragCoeff):
        super().__init__(categorie, name, imageFile)
        self.__mass = mass
        self.__length = length
        self.__projectedArea = projectedArea
        self.__normalDragCoeff = normalDragCoeff
        self.__tangentialDragCoeff = tangentialDragCoeff

    def creationElement(self) -> UnmodifiableElement:
        return UnmodifiableElement(self)

    @property
    def mass(self):
        return self.__mass

    @property
    def length(self):
        return self.__length

    @property
    def projectedArea(self):
        return self.__projectedArea

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff
