# Classe Transicao

class Transition(object):

    def __init__(self, From, To, Read):
        self.From = From
        self.To = To
        self.Read = Read

    def getFrom(self):
        return self.From

    def getTo(self):
        return self.To

    def getRead(self):
        return self.Read

    def setFrom(self, From):
        self.From = From

    def setTo(self, To):
        self.To = To

    def setRead(self, Read):
        self.Read = Read

    def printTransition(self):
        return self.From + "->" + self.To + "," + self.Read + " | "