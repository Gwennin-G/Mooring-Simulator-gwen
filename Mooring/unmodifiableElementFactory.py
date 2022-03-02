from xml.etree.ElementTree import Element
from factory import Factory

class UnmodifiableElementFactory(Factory):

    def __init__(self,categorie,name,imageFile,mass,length,projectedArea,normalArea,normaDragCoeff,tangentialDragCoeff):
        super().__init__(categorie,name,imageFile)
        self.__mass__ = mass
        self.__length__ = length
        self.__projectedArea__ = projectedArea
        self.__normalArea__ = normalArea
        self.__normalDragCoeff__ = normaDragCoeff
        self.__tangentialDragCoeff__ = tangentialDragCoeff

    def creationElement(self) -> Element:
        return Element(self)
