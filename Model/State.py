# Classe Estado

class Estado(object):

    def __init__(self, Id, Name, Final, Initial):
        self.Id = Id
        self.Name = Name
        self.Final = Final
        self.Initial = Initial

    def __get__(self, Name):
        return self.Name

    #def getName(self):
    #    return self.Name






