import sys
from mooring.unmodifiableElement import UnmodifiableElement
from library.unmodifiableElementFactory import UnmodifiableElementFactory


uef = UnmodifiableElementFactory("LPO","microcat","\Pictures\Instrument\microcat.bmp",-3,0.6,0.03,1.3,0.9)
print("objet : unmodifiable element factory",
    "\ncategorie : ", uef.category ,
    "\nname : ", uef.name ,
    "\nimage : ", uef.imageFile, 
    "\nmasse : " , uef.mass, 
    "\nlongueur : ", uef.length,
    "\naire projetée : ", uef.projectedArea,
    "\ncoeff normal : ", uef.normalDragCoeff,
    "\ncoeff tangentiel : ", uef.tangentialDragCoeff
    ,"\n")

ue =uef.creationElement()
print("objet : unmodifiable element :", isinstance(ue,UnmodifiableElement),
    "\ncategorie : ", ue.category ,
    "\nname : ", ue.name ,
    "\nimage : ", ue.imageFile, 
    "\nmasse : " , ue.mass, 
    "\nlongueur : ", ue.length,
    "\naire projetée : ", ue.projectedArea,
    "\ncoeff normal : ", ue.normalDragCoeff,
    "\ncoeff tangentiel : ", ue.tangentialDragCoeff)

