from element import Element
from library.unmodifiableElementFactory import UnmodifiableElementFactory

class UnmodifiableElement(Element):
    def __init__(self, factory):
        if isinstance(factory, UnmodifiableElementFactory):
            super().__init__()
            self.__factory__ = factory

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
        return self.__factory__.mass

    @property
    def length(self):
        return self.__factory__.length

    @property
    def projectedArea(self):
        return self.__factory__.projectedArea

    @property
    def normalDragCoeff(self):
        return self.__factory__.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory__.tangentialDragCoeff