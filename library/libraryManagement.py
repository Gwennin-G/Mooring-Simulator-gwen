from library.library import Library

class LibraryManagement():
    def __init__(self):
        self.__library = Library()

    def newFactory(self, type, parameter):
        self.__library.newFactory(type, parameter)

    def createElement(self, libraryName, parameters):
        self.__library.createElement(libraryName, parameters)
    
    def getDisplayDataByName(self, name):
        imageFile = self.__library.getFactoryImageFile(name)
        return{'name' : name, 'imageFile' : imageFile}

    def getAllDisplayData(self):
        nameList = self.__library.getAllFactoryKey()
        data = list()
        for name in nameList:
            data.append(self.getDisplayDataByName(name))
