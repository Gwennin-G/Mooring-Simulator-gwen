
from library.unmodifiableElementFactory import UnmodifiableElementFactory
from library.ropeElementFactory import RopeElementFactory
from library.massDependantElementFactory import MassDependantElementFactory
from mooring.element import Element

class Library():
    def __init__(self):
        self.__factories = {}

    def newFactory(self, type, parameters):
        if type == "Terminals" or type =="Floats" or type =="Instruments" or type =="Releases" :  
            self.__factories[parameters['name']] = UnmodifiableElementFactory(parameters["categorie"],
                                                                            parameters["name"],
                                                                            parameters["imageFile"],
                                                                            parameters["mass"],
                                                                            parameters["length"],
                                                                            parameters["projectedArea"],
                                                                            parameters["normalDragCoeff"],
                                                                            parameters["tangentialDragCoeff"]
                                                                            )
        elif type == "Ropes":
            self.self.__factories[parameters['name']] = RopeElementFactory(parameters["categorie"],
                                                                            parameters["name"],
                                                                            parameters["imageFile"],
                                                                            parameters["mass"],
                                                                            parameters["diameter"],
                                                                            parameters["projectedArea"],
                                                                            parameters["normalDragCoeff"],
                                                                            parameters["tangentialDragCoeff"],
                                                                            parameters["stretchCoeff"],
                                                                            parameters["breakingStretch"]
                                                                            )
        elif type == "Anchors":
            self.self.__factories[parameters['name']] = MassDependantElementFactory(parameters["categorie"],
                                                                                    parameters["name"],
                                                                                    parameters["imageFile"],
                                                                                    parameters["length"],
                                                                                    parameters["diameter"],
                                                                                    parameters["projectedArea"],
                                                                                    parameters["normalDragCoeff"],
                                                                                    parameters["tangentialDragCoeff"])

    def createElement(self, libraryName, parameters) -> Element:
        if libraryName in self.__factories.keys():
            return self.__factories[libraryName].creationElement(parameters)

    def getAllFactoryKey(self):
        return self.__factories.keys

    def getFactoryImageFile(self, name):
        if name in self.__factories.keys:
            return self.__factories[name].imageFile
        else :
            raise KeyError('name')