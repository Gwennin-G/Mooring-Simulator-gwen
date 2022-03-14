'''this class manage specific functionnality for the RopeElement creation'''

from mooring.ropeElement import RopeElement
from library.factory import Factory


class RopeElementFactory(Factory):

    '''Factory contains most of the parameters of elements their create'''
    def __init__(self, categorie, name, imageFile, mass, diameter, projectedArea, normalDragCoeff, tangentialDragCoeff, stretchCoeff, breakingStretch):
        super().__init__(categorie, name, imageFile)
        self.__massByLength = mass
        self.__diameter = diameter
        self.__projectedAreaByLength = projectedArea
        self.__normalDragCoeff = normalDragCoeff
        self.__tangentialDragCoeff = tangentialDragCoeff
        self.__stretchCoeff = stretchCoeff
        self.__breakingStretch = breakingStretch

    '''Parameters must be a dictionary with a 'length' key '''
    def creationElement(self, parameters) -> RopeElement:
        if "length" in parameters.keys():
            if parameters["length"] is None or parameters["length"] == 0:
                return RopeElement(self, True, 0)
            else :
                return RopeElement(self, False, parameters["length"])
        else :
            raise KeyError('length')

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