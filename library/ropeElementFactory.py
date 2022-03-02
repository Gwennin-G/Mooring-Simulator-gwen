from mooring.ropeElement import RopeElement
from library.factory import Factory


class RopeElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,mass,projectedArea,diameter,normaDragCoeff,tangentialDragCoeff,stretchCoeff,breakingStretch):
        super().__init__(categorie,name,imageFile)
        self.__massByLenght__ = mass
        self.__projectedAreaByLenght__ = projectedArea
        self.__diameter__ = diameter
        self.__normalDragCoeff__ = normaDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff
        self.__stretchCoeff__ = stretchCoeff
        self.__breakingStretch__ = breakingStretch

    def creationElement(self,lenght) -> RopeElement:
        if lenght is None:
            return RopeElement(self,False,0)
        else :
            return RopeElement(self,True,lenght)

    @property
    def massByLenght(self):
        return self.__massByLenght__

    @property
    def projectedAreaByLenght(self):
        return self.__projectedAreaByLenght__

    @property
    def diameter(self):
        return self.__diameter__

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff__

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff__

    @property
    def stretchCoeff(self):
        return self.__stretchCoeff__

    @property
    def breakingStretch(self):
        return self.__breakingStretch__