from library.factory import Factory
from mooring.massDependantElement import MassDependantElement

class MassDependantElementFactory(Factory):

    def __init__(self, categorie, name, imageFile, length, diameter , projectedArea, normaDragCoeff, tangentialDragCoeff):
        super().__init__(categorie, name, imageFile)
        self.__length = length
        self.__diameter = diameter
        self.__projectedArea = projectedArea
        self.__normalDragCoeff = normaDragCoeff
        self.__tangentialDragCoeff = tangentialDragCoeff

    def creationElement(self, parameters) -> MassDependantElement:
        if "mass" in parameters.keys():
            return MassDependantElement(self,parameters["mass"])
        else :
            raise KeyError('mass')

    @property
    def length(self):
        return self.__length

    @property
    def diameter(self):
        return self.__diameter

    @property
    def projectedArea(self):
        return self.__projectedArea

    @property
    def diameter(self):
        return self.__diameter

    @property
    def normalDragCoeff(self):
        return self.__normalDragCoeff

    @property
    def tangentialDragCoeff(self):
        return self.__tangentialDragCoeff


if __name__ == '__main__':
    mef = MassDependantElementFactory("LPO", "rain train", "\Pictures\Anchors\lest.bmp", 1, 1, 0.785, 1.2 ,1 )
    print("objet : Mass dependant element factory",
    "\ncategorie : ", mef.category ,
    "\nname : ", mef.name ,
    "\nimage : ", mef.imageFile, 
    "\nlongueur : ", mef.length,
    "\naire projetée : ", mef.projectedArea,
    "\ncoeff normal : ", mef.normalDragCoeff,
    "\ncoeff tangentiel : ", mef.tangentialDragCoeff
    ,"\n")