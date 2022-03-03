import sys
from mooring.massDependantElement import MassDependantElement
from library.massDependantElementFactory import MassDependantElementFactory


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

me =mef.creationElement(1000)
print("objet : Mass dependant element :", isinstance(me,MassDependantElement),
    "\ncategorie : ", me.category ,
    "\nname : ", me.name ,
    "\nimage : ", me.imageFile, 
    "\nmasse : " , me.mass, 
    "\nlongueur : ", me.length,
    "\naire projetée : ", me.projectedArea,
    "\ncoeff normal : ", me.normalDragCoeff,
    "\ncoeff tangentiel : ", me.tangentialDragCoeff)