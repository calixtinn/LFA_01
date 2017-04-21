"""
@AFDController
@author: Matheus Calixto | Samuel Terra
Classe que implementa todas as funcionalidade um Automoto Finito Deterministico.
"""
import xml.etree.ElementTree as ET
from Model.State import State
from Model.Transition import Transition
from Model.AFD import AFD

class AFDController(object):

    def __init__(self):
        """
        Inicializa as variaveis de classe
        """
        self.states = []  # Lista de estados
        self.transitions = []  # Lista de transições
        self.finals = []  # Lista de estados finais
        self.alphabet = []  # alfabeto que o automato suporta

    def load(self, jffFile, cont):
        """
        Metodo responsavel por ler um arquivo XML em formato jff conteudo o AFD.
        :param jffFile
        :param cont
        :rtype AFD
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
        """
        Metodo responsavel por salvar AFD em um arquivo XML em formato jff.
        :param jffFile
        :param cont
        :rtype bool
        """
        pass

    def equivalents(self):
        """
        Metodo responsavel por verificar os estados equivalentes do AFD.
        :rtype list
        """
        pass

    def minimum(self):
        """
        Metodo responsavel por realizar a minimização do AFD.
        :rtype AFD
        """
        pass

    def equivalent(self, m1, m2):
        """
        Metodo responsavel por verificar a equivalencia de dois AFDs.
        :param m1
        :param m2
        :rtype bool
        """
        pass

    def complement(self):
        """
        Metodo responsavel por realizar o complemento AFD.
        :rtype AFD
        """
        pass

    def union(self, m2):
        """
        Metodo responsavel por realizar a união do AFD da classe com um outro.
        :param m2
        :rtype AFD
        """
        pass

    def intersection(self, m2):
        """
        Metodo responsavel por realizar a interseção do AFD da classe com um outro.
        :param m2
        :rtype AFD
        """
        pass

    def difference(self, m2):
        """
        Metodo responsavel por realizar a diferença do AFD da classe com um outro.
        :param m2
        :rtype AFD
        """
        pass

    def accept(self, word):
        """
        Metodo responsavel por verificar se uma determinada palavra é aceita pelo AFD.
        :param word
        :rtype bool
        """
        pass

    def initial(self):
        """
        Metodo responsavel por retornar o estado inicial do AFD.
        :rtype State
        """
        pass

    def move(self):
        """
        xxxxxxx
        :rtype 
        """
        pass

    def finals(self):
        """
        Metodo responsavel por retornar os estados finais do AFD.
        :rtype list
        """
        pass

    def addState(self, id, initial, final):
        """
        Metodo responsavel por adicionar estado ao AFD.
        :param id
        :param initial
        :param final
        :rtype bool
        """
        pass

    def addTransition(self, source, target, consume):
        """
        Metodo responsavel por adicionar transições ao AFD.
        :param source
        :param target
        :param consume
        :rtype bool
        """
        pass

    def deleteState(self, id):
        """
        Metodo responsavel por deletar um estado do AFD.
        :param id
        :rtype: bool
        """
        pass

    def deleteTransition(self, source, target, consume):
        """
        Metodo responsavel por deletar uma transição de um estado a outro.
        :param source
        :param target
        :param consume
        :rtype bool
        """
        pass
