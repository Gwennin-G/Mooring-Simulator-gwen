from mooring.element import Element


class RopeElement(Element):
    def __init__(self, factory,fixe,lenght):
        super().__init__()
        self.__factory__ = factory
        self.__lenghtIsFixe__ = fixe
        self.__lenght__ = lenght

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
        return self.__factory__.massByLenght * self.__lenght__

    @property
    def length(self):
        return self.__lenght__

    @property
    def diameter(self):
        return self.__factory__.diameter

    @property
    def projectedArea(self):
        return self.__factory__.projectedAreaByLenght * self.__lenght__

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