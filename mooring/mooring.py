from msilib.schema import Property
from typing import List
from mooring.element import Element

class Mooring():
    def __init__(self):
        self.__elements = []
        self.__firstElement = None

    def getElementList(self):
        return self.__elements

    def getElementsAfter(self,element):
        elements = []
        for link in element.after:
            elements.append(link.after)
        return elements

    def getElementsbefore(self,element):
        return element.before.before

    @Property
    def FirstElement(self):
        return self.__firstElement

    def getElementOrder(self):
        elementOrder = []
        elementsNext =[]
        elements = []
        elements.append(self.FirstElement)
        while elements is not []:
            for element in elements:
                elementOrder.append(element)
                elementsNext.extend(self.getElementsAfter)
            elements = elementsNext
            elementsNext.clear
        return elementOrder

    def getDataElement(self,element):
        return {"name":element.name,"image":element.imageFile}

    def addElement(self,previousElement,element,nextElement):
        self.__elements.append(element)
        if previousElement is None:
            self.__firstElement = element
        else:
            element.before = previousElement
            previousElement.removeAfter(nextElement)
        if nextElement is None:
            element.addAfter(nextElement)
        else:
           element.after = nextElement
           nextElement.before = previousElement
        
