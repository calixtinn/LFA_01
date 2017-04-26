"""
@Transition
@author: Matheus Calixto | Samuel Terra
Esta classe representa uma Transição (ligação) de Estados em um Automato.
"""

class Transition(object):

    def __init__(self, Id, From, To, Read):
        self.Id = Id
        self.From = From
        self.To = To
        self.Read = Read

    def getFrom(self):
        return self.From

    def getTo(self):
        return self.To

    def getRead(self):
        return self.Read

    def getId(self):
        return self.Id

    def setFrom(self, From):
        self.From = From

    def setTo(self, To):
        self.To = To

    def setRead(self, Read):
        self.Read = Read

    def printTransition(self):
        return "(" + str(self.Id) + ")  " + self.From + "->" + self.To + "," + self.Read + " | "