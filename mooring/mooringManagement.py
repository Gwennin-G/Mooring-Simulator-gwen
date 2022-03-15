'''cette classe ne correspond pas totalement aux fonctionnalitées de la conception '''
from mooring.mooring import Mooring

class MooringManagement():

    def __init__(self):
        self.mooring = Mooring()

    def getDataElement(self,element):
        return self.mooring.getDataElement(element)

    def getElementOrder(self):
        return self.mooring.getElementOrder()

    def getAllDataElement(self):
        elements = self.getElementOrder()
        dataElements = [elements]
        for element in elements:
            dataElements.append(self.getDataElement(element))
        return dataElements

    def addElement(self,previousElement,element,nextElement):
        self.mooring.addElement(previousElement,element,nextElement)