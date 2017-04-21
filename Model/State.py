# Classe Estado

class State(object):

    def __init__(self, Id, Name, Initial, Final):
        self.Id = Id
        self.Name = Name
        self.Final = Final
        self.Initial = Initial

    def getId(self):
        return self.Id

    def getName(self):
        return self.Name

    def isFinal(self):
        return self.Final

    def isInitial(self):
        return self.Initial

    def setId(self, Id):
        self.Id = Id

    def setName(self, Name):
        self.Name = Name

    def setFinal(self, Final):
        self.Final = Final

    def setInitial(self, Initial):
        self.Initial = Initial








