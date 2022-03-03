from mooring.element import Element


class RopeElement(Element):
    def __init__(self, factory,fixe,length):
        super().__init__()
        self.__factory__ = factory
        self.__lengthIsFixe__ = fixe
        self.__length__ = length

    @property
    def name(self):
        return self.__factory__.name

    @property
    def category(self):
         return self.__factory__.category

    @property
    def imageFile(self):
        return self.__factory__.imageFile

    @property
    def mass(self):
        return self.__factory__.massByLength * self.__length__

    @property
    def length(self):
        return self.__length__

    @property
    def diameter(self):
        return self.__factory__.diameter

    @property
    def projectedArea(self):
        return self.__factory__.projectedAreaByLength * self.__length__

    @property
    def normalDragCoeff(self):
        return self.__factory__.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory__.tangentialDragCoeff

    @property
    def stretchCoeff(self):
        return self.__factory__.stretchCoeff

    @property
    def breakingStretch(self):
        return self.__factory__.breakingStretch