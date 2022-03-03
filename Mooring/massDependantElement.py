from mooring.element import Element

class MassDependantElement(Element):
    def __init__(self, factory,mass):
        super().__init__()
        self.__factory__ = factory
        self.__mass__ = mass

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
        return self.__mass__

    @property
    def length(self):
        return self.__factory__.length

    @property
    def diameter(self):
        return self.__factory__.diameter

    @property
    def projectedArea(self):
        return self.__factory__.projectedArea

    @property
    def normalDragCoeff(self):
        return self.__factory__.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory__.tangentialDragCoeff