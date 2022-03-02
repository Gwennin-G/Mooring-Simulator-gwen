from element import Element

class UnmodifiableElement(Element):
    def __init__(self, factory):
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
    def diameter(self):
        return self.__factory__.diameter

    @property
    def projectedArea(self):
        return self.__factory__.cateprojectedAreagory

    @property
    def normalDragCoef(self):
        return self.__factory__.normalDragCoef

    @property
    def tangentialCoef(self):
        return self.__factory__.tangentialCoef