from mooring.element import Element

class MassDependantElement(Element):
    def __init__(self, factory, mass):
        super().__init__()
        self.__factory = factory
        self.__mass = mass

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
        return self.__mass

    @mass.setter
    def mass(self, newMass):
        self.__mass  = newMass

    @property
    def length(self):
        return self.__factory.length

    @property
    def diameter(self):
        return self.__factory.diameter

    @property
    def projectedArea(self):
        return self.__factory.projectedArea

    @property
    def normalDragCoeff(self):
        return self.__factory.normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__factory.tangentialDragCoeff