import sys

from mooring.element import Element


class UnmodifiableElement(Element):
    def __init__(self, factory):
        super().__init__()
        self.__factory = factory

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
        return self.__factory.mass

    @property
    def length(self):
        return self.__factory.length

    @property
    def projectedArea(self):
        return self.__factory.projectedArea

    @property
    def normalDragCoeff(self):
        return self.__factory.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory.tangentialDragCoeff