# Classe Estado

class State(object):

    def __init__(self, Id, Name, Final, Initial):
        self.Id = Id
        self.Name = Name
        self.Final = Final
        self.Initial = Initial

    def getName(self):
        return self.Name






