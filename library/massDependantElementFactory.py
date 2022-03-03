from library.factory import Factory
from mooring.massDependantElement import MassDependantElement

class MassDependantElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,length,diameter,projectedArea,normaDragCoeff,tangentialDragCoeff):
        super().__init__(categorie,name,imageFile)
        self.__length__ = length
        self.__diameter__ = diameter
        self.__projectedArea__ = projectedArea
        self.__normalDragCoeff__ = normaDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff

    def creationElement(self,mass) -> MassDependantElement:
            return MassDependantElement(self,mass)

    @property
    def length(self):
        return self.__length__

    @property
    def diameter(self):
        return self.__diameter__

    @property
    def projectedArea(self):
        return self.__projectedArea__

    @property
    def diameter(self):
        return self.__diameter__

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff__

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff__