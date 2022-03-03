from mooring.ropeElement import RopeElement
from library.factory import Factory


class RopeElementFactory(Factory):

    def __init__(self, categorie, name, imageFile, mass, diameter, projectedArea, normaDragCoeff, tangentialDragCoeff, stretchCoeff, breakingStretch):
        super().__init__(categorie, name, imageFile)
        self.__massByLength = mass
        self.__diameter = diameter
        self.__projectedAreaByLength = projectedArea
        self.__normalDragCoeff = normaDragCoeff
        self.__tangentialDragCoeff = tangentialDragCoeff
        self.__stretchCoeff = stretchCoeff
        self.__breakingStretch = breakingStretch

    def creationElement(self, length) -> RopeElement:
        if length is None or length == 0:
            return RopeElement(self, True, 0)
        else :
            return RopeElement(self, False, length)

    @property
    def massByLength(self):
        return self.__massByLength

    @property
    def diameter(self):
        return self.__diameter

    @property
    def projectedAreaByLength(self):
        return self.__projectedAreaByLength

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff

    @property
    def stretchCoeff(self):
        return self.__stretchCoeff

    @property
    def breakingStretch(self):
        return self.__breakingStretch