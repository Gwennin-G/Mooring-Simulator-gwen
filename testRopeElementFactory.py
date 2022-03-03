import sys
from mooring.ropeElement import RopeElement
from library.ropeElementFactory import RopeElementFactory


ref = RopeElementFactory("LPO","parafil kevlar 8,5 mm","\Pictures\Ropes\cable.bmp",-0.0034,0.0085,0.0085,1.3,0.1,[0,0.031428571,0],3000)
print("objet : unmodifiable element factory",
    "\ncategorie : ", ref.category ,
    "\nname : ", ref.name ,
    "\nimage : ", ref.imageFile, 
    "\nmasse par metre : ", ref.massByLenght, 
    "\ndiametre : ", ref.diameter,
    "\naire projetée par metre : ", ref.projectedAreaByLenght,
    "\ncoeff normal : ", ref.normalDragCoeff,
    "\ncoeff tangentiel : ", ref.tangentialDragCoeff,
    "\ncoeff etirement : ", ref.stretchCoeff,
    "\nrupture : ", ref.breakingStretch,
    "\n")

re = ref.creationElement(100)
print("objet : rope element :", isinstance(re,RopeElement),
    "\ncategorie : ", re.category ,
    "\nname : ", re.name ,
    "\nimage : ", re.imageFile, 
    "\nmasse : " , re.mass, 
    "\nlongueur : ", re.length,
    "\ndiameter : ", re.diameter,
    "\naire projetée : ", re.projectedArea,
    "\ncoeff normal : ", re.normalDragCoeff,
    "\ncoeff tangentiel : ", re.tangentialDragCoeff,
    "\ncoeff etirement : ", re.stretchCoeff,
    "\nrupture : ", re.breakingStretch,
    "\n")

