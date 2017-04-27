"""
@State
@author: Matheus Calixto | Samuel Terra
Esta classe representa um Estado em um Automoto.
"""

from Model.Transition import Transition

class State(object):
    def __init__(self, Id, Name, Posx, Posy, Initial, Final):
        self.Id = Id
        self.Name = Name
        self.Posx = Posx
        self.Posy = Posy
        self.Final = Final
        self.Initial = Initial

    def getId(self):
        return self.Id

    def getName(self):
        return self.Name

    def getPosx(self):
        return self.Posx

    def getPosy(self):
        return self.Posy

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

    def setPosx(self, Posx):
        self.Posx = Posx

    def setPosy(self, Posy):
        self.Posy = Posy

    def printState(self):
        print("Estado: " + self.getName() + "\nID: " + self.getId() +
              "\nPosição X: " + self.getPosx() + "\nPosição Y: " + self.getPosy() +
              "\nInicial: " + str(self.isInitial()) + "\nFinal: " + str(self.isFinal()))