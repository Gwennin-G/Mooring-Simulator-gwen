from library.factory import Factory
from mooring.massDependantElement import MassDependantElement

class MassDependantElementFactory(Factory):

    def __init__(self, categorie, name, imageFile, length, diameter , projectedArea, normaDragCoeff, tangentialDragCoeff):
        super().__init__(categorie, name, imageFile)
        self.__length = length
        self.__diameter = diameter
        self.__projectedArea = projectedArea
        self.__normalDragCoeff = normaDragCoeff
        self.__tangentialDragCoeff = tangentialDragCoeff

    def creationElement(self, mass) -> MassDependantElement:
            return MassDependantElement(self,mass)

    @property
    def length(self):
        return self.__length

    @property
    def diameter(self):
        return self.__diameter

    @property
    def projectedArea(self):
        return self.__projectedArea

    @property
    def diameter(self):
        return self.__diameter

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff