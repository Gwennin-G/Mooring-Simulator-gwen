from mooring.element import Element


class RopeElement(Element):
    def __init__(self, factory, automatic, length):
        super().__init__()
        self.__factory = factory
        self.__lengthIsAutomatic = automatic
        self.__length = length

    @property
    def name(self):
        return self.__factory.name

    @property
    def category(self):
         return self.__factory.category

    @property
    def imageFile(self):
        return self.__factory.imageFile

    @property
    def mass(self):
        return self.__factory.massByLength * self.__length

    @property
    def lengthIsAutomatic(self):
        return self.__lengthIsAutomatic

    @lengthIsAutomatic.setter
    def lengthIsAutomatic(self, isAutomatic):
        self.__lengthIsAutomatic = isAutomatic

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, newLength):
        self.__lengthIsAutomatic = False
        self.__length = newLength

    @property
    def diameter(self):
        return self.__factory.diameter

    @property
    def projectedArea(self):
        return self.__factory.projectedAreaByLength * self.__length

    @property
    def normalDragCoeff(self):
        return self.__factory.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory.tangentialDragCoeff

    @property
    def stretchCoeff(self):
        return self.__factory.stretchCoeff

    @property
    def breakingStretch(self):
        return self.__factory.breakingStretch