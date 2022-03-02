from mooring.ropeElement import RopeElement
from library.factory import Factory


class RopeElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,mass,projectedArea,normalArea,normaDragCoeff,tangentialDragCoeff):
        super().__init__(categorie,name,imageFile)
        self.__mass__ = mass
        self.__projectedArea__ = projectedArea
        self.__normalArea__ = normalArea
        self.__normalDragCoeff__ = normaDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff

    def creationElement(self,lenght) -> RopeElement:
        if lenght is None:
            return RopeElement(self,False,0)
        else :
            return RopeElement(self,True,lenght)

    @property
    def mass(self):
        return self.__mass__

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