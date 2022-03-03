from mooring.element import Element


class RopeElement(Element):
    def __init__(self, factory,automatic,length):
        super().__init__()
        self.__factory__ = factory
        self.__lengthIsAutomatic__ = automatic
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
    def lengthIsAutomatic(self):
        return self.__lengthIsAutomatic__

    @lengthIsAutomatic.setter
    def lengthIsAutomatic(self,isAutomatic):
        self.__lengthIsAutomatic__ = isAutomatic

    @property
    def length(self):
        return self.__length__

    @length.setter
    def length(self,newLength):
        self.__lengthIsAutomatic__=False
        self.__length__ = newLength

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