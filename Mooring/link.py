

class Link():

    def __init__(self, before, after):
        self.__before = before
        self.__after = after

    @property
    def before(self) :
        return self.__before

    @before.setter
    def before(self, newElement) :
        self.__before = newElement

    @property
    def after(self) :
        return self.__after

    @after.setter
    def after(self, newElement) :
        self.__after = newElement