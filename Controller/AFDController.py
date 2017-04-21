"""
@AFDController
@author: Matheus Calixto | Samuel Terra
Esta classe implementa todas as funcionalidade um Automoto Finito Deterministico.
"""

import xml.etree.ElementTree as ET
from Model.State import State
from Model.Transition import Transition
from Model.AFD import AFD


class AFDController(object):

    def __init__(self):
        self.states = []  # Lista de estados
        self.transitions = []  # Lista de transições
        self.finals = []  # Lista de estados finais
        self.alphabet = []  # alfabeto que o automato suporta

    def load(self, jffFile, cont):
        """
        Este metodo é responsavel por ler um arquivo XML em formato jff contendo o AFD.
        :return @AFD
        """

        s_initial = ""  # Guardará o ID do estado inicial
        doc = ET.parse("Input/" + jffFile)  # Recebendo o arquivo de entrada via parametro da função.
        root = doc.getroot()  # Recebendo a tag root

        # iterando em cada tag State para pegar as informações
        for i in root.iter('state'):

            x = i.find('x').text
            y = i.find('y').text
            name = i.attrib['name']
            id = i.attrib['id']

            # Se nesse estado houver a tag inicial, seta o estado como inicial.
            if (i.find('initial') != None):
                initial = True
                s_initial = id
            else:
                initial = False

            # Se nesse estado houver a tag final, seta o estado como final.
            if (i.find('final') != None):
                final = True
                self.finals.append(id)
            else:
                final = False

            # Cria um objeto Estado
            state = State(id, name, x, y, initial, final)

            # Adiciona na lista de estados
            self.states.append(state)

        # Fim da obtenção das informações referentes aos estados

        # Iterando na tag <transition>
        # Pegando as transições
        for i in root.iter('transition'):
            From = i.find('from').text
            To = i.find('to').text
            Read = i.find('read').text

            # Adiciona o caractere lido na lista do alfabeto
            self.alphabet.append(Read)

            transition = Transition(From, To, Read)
            self.transitions.append(transition)
        # Fim da obtenção das informações referentes às transições.

        alphabet = list(set(self.alphabet))
        automato = AFD(cont, self.states, self.transitions, s_initial, self.finals, alphabet)  # Cria um automato

        return automato

    def save(self, jffFile, cont):
        pass

    def equivalents(self):
        pass

    def minimum(self):
        pass

    def equivalent(self, m1, m2):
        pass

    def complement(self):
        pass

    def union(self, m2):
        pass

    def intersection(self, m2):
        pass

    def difference(self, m2):
        pass

    def accept(self, word):
        pass

    def initial(self):
        pass

    def move(self):
        pass

    def finals(self):
        pass

    def addState(self):
        pass

    def addTransition(self):
        pass

    def deleteState(self):
        pass

    def deleteTransition(self):
        pass
