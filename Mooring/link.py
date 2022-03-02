

class Link():

    def __init__(self, before, after):
        self.__before__ = before
        self.__after__ = after

    @property
    def before(self) :
        return self.__before__

    @before.setter
    def before(self, newElement) :
        self.__before__ = newElement

    @property
    def after(self) :
        return self.__after__

    @after.setter
    def after(self, newElement) :
        self.__after__ = newElement