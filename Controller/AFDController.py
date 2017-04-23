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

    automata_Id_counter = 0

    def __init__(self):
        """
        Inicializa as variaveis de classe
        """
        self.states = []  # Lista de estados
        self.transitions = []  # Lista de transições
        self.finals = []  # Lista de estados finais
        self.alphabet = []  # alfabeto que o automato suporta

    def load(self, jffFile):
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
        automato = AFD(AFDController.automata_Id_counter, self.states, self.transitions, s_initial, self.finals, alphabet)  # Cria um automato

        AFDController.automata_Id_counter += 1

        return automato

    def save(self, jffFile, cont):
        """
        Metodo responsavel por salvar AFD em um arquivo XML em formato jff.
        :param jffFile
        :param cont
        :rtype bool
        """
        pass

    def equivalents(afd):
        """
        Metodo responsavel por verificar os estados equivalentes do AFD.
        :param afd
        :rtype list
        """
        matriz_equivalencia = []
        possiveis_equivalentes = []
        transicoes_possiveis_eq = [] #transicoes dos estados que possivelmente seriam equivalentes

        estados = afd.getStates()   #recebe uma lista com os estados do automato
        alfabeto = afd.getAlphabet()#recebe uma lista contendo o alfabeto do automato
        transicoes = afd.getTransitions() #recebe uma lista contendo as transições do autômato

        n_estados = len(estados)    #salva o número de estados do autômato
        n_simbolos = len(alfabeto)  #salva o número de símbolos do alfabeto do autômato.


        #cria e inicializa a matriz de equivalência.

        #I  = Igual. Ex: (1,1), (2,2)...
        #N  = Espaço em branco
        #X  = Não equivalente
        #O  = Possível equivalencia

        for linha in range(0, n_estados):
            aux = []
            for coluna in range(0, n_estados):
                if(linha == coluna):
                    aux.append("I") #I de igual
                elif(estados[linha].isFinal() != estados[coluna].isFinal()): #Compara-se estados finais com não finais.
                    aux.append("X")
                else:
                    aux.append("N") #espaço em branco.
                    possiveis_equivalentes.append(str(coluna))

            matriz_equivalencia.append(aux)

        possiveis_equivalentes = list(set(possiveis_equivalentes)) #Lista os estados que devem ser testados entre si.
        n_possiveis_eq = len(possiveis_equivalentes) #tamanho da lista de possíveis equivalentes.

        #Salva numa lista todas as transições dos estados que possívelmente são equivalentes.
        for i in transicoes:
            for j in range(0,n_possiveis_eq):
                if(i.getFrom() == possiveis_equivalentes[j]):
                    transicoes_possiveis_eq.append(i)

        for i in range(0, n_possiveis_eq):
            for j in range(i+1, n_possiveis_eq):
                trans_i = []  # transicoes de i
                trans_j = []  # transicoes de j
                for k in transicoes_possiveis_eq: #procura as transições dos respectivos estados
                    if(k.getFrom() == possiveis_equivalentes[i]):
                        trans_i.append([k.getTo(), k.getRead()]) #recebe o destino e o caractere lido
                    if(k.getFrom() == possiveis_equivalentes[j]):
                        trans_j.append([k.getTo, k.getRead])

        #fazendo.... pode deixar que eu faço essa função man!
        return len(transicoes_possiveis_eq)

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
