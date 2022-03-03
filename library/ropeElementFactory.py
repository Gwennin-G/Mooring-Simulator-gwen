from mooring.ropeElement import RopeElement
from library.factory import Factory


class RopeElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,mass,diameter,projectedArea,normaDragCoeff,tangentialDragCoeff,stretchCoeff,breakingStretch):
        super().__init__(categorie,name,imageFile)
        self.__massByLength__ = mass
        self.__diameter__ = diameter
        self.__projectedAreaByLength__ = projectedArea
        self.__normalDragCoeff__ = normaDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff
        self.__stretchCoeff__ = stretchCoeff
        self.__breakingStretch__ = breakingStretch

    def creationElement(self,length) -> RopeElement:
        if length is None or length == 0:
            return RopeElement(self,True,0)
        else :
            return RopeElement(self,False,length)

    @property
    def massByLength(self):
        return self.__massByLength__

    @property
    def diameter(self):
        return self.__diameter__

    @property
    def projectedAreaByLength(self):
        return self.__projectedAreaByLength__

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