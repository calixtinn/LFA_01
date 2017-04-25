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
        tabela_equivalencia = {} #Tabela que contem a quivalência entre os estados
        lista_estados = [] #lista para o controle dos estados
        transicoes_estados = [] #transicoes dos estados
        lista_equivalentes = [] #lista de estados equivalentes
        amarrados = {} #Dicionario contendo as amarrações entre estados no algoritmo de equivalencia.

        estados = afd.getStates()   #recebe uma lista com os estados do automato (OBJETOS)
        alfabeto = afd.getAlphabet()#recebe uma lista contendo o alfabeto do automato
        transicoes = afd.getTransitions() #recebe uma lista contendo as transições do autômato

        #Cria e inicializa a tabela Hash de equivalências

        for estado in estados: #para cada estado na lista OBJETOS de estados
            lista_estados.append(estado.getId())

        n_estados = len(lista_estados)  # tamanho da lista de estados

        for i in range(0, n_estados): #Percorre a lista de estados testando-os um a um
            e1 = lista_estados[i]
            for j in range(i+1, n_estados):
                e2 = lista_estados[j]
                chave = e1+","+e2 #Cria uma chave para se testar na tabela. Ex: 1,2 (Estado1 equivalente a estado 2?)
                if (estados[i].isFinal() != estados[j].isFinal()): #Se ambos não forem finais ou não finais já não é equivalente
                    tabela_equivalencia[chave] = "X" #Marca na tabela Hash que não é equivalente.
                else: tabela_equivalencia[chave] = "N" # Caso contrário, marca como N (Espaço vazio a ser testado)
        #CRIADA A TABELA

        #Salva em uma lista as todas as transições de todos os estados.
        for i in transicoes:
            for j in range(0, n_estados):
                if (i.getFrom() == lista_estados[j]):
                    transicoes_estados.append(i)

        for i in range(0, n_estados):  # Percorre a lista de estados
            trans_i = {}  # transicoes de i (dicionario)
            for k in transicoes_estados:  # procura as transições dos respectivos estados
                if (k.getFrom() == lista_estados[i]):
                    trans_i[k.getRead()] = k.getTo()  # Ex: ["a"] = 1 [caractere] = para onde vai.
            # End pegar transições de I

            for j in range(i + 1, n_estados):  # Segundo for para percorrer a lista e testar um a um

                # Os estados precisam ser iguais (final e final) ou (não final e não final) para testar
                # Se não forem, quer dizer que eles já não são equivalentes e não precisa-se testar.

                if (estados[i].isFinal() == estados[j].isFinal()):

                    trans_j = {}  # transicoes de j (dicionario)
                    for k in transicoes_estados:  # procura as transições dos respectivos estados
                        if (k.getFrom() == lista_estados[j]):
                            trans_j[k.getRead()] = k.getTo()
                    # End pegar transições de j

                    for a in alfabeto:  # Para cada caracter do alfabeto...

                        if (a in trans_i and a in trans_j):  # Se houver transições com o caractere do alfabeto em ambos os estados.

                            destino_i = trans_i[a]  # Salva o destino do estado i ao ler o caractere em questão
                            destino_j = trans_j[a]  # Faz o mesmo para o estado j
                            chave_destino = destino_i + "," + destino_j #cria uma chave para testar na tabela

                            '''
                             Verifica se não acontecem inconssistências do tipo:
                             Estou testando estados 0 e 1:
                                a
                             0
                             1

                             se ao ler um caractere a eu for para :
                                a
                             0  1
                             1  0

                             Não faz sentido testar esta equivalência entre 0,1 e 1,0.
                            '''
                            if (destino_i != lista_estados[j]):

                                estado_i = lista_estados[i]
                                estado_j = lista_estados[j]
                                possivel_chave = estado_i + "," + estado_j #Cria-se uma chave para marcar na tabela

                                if(destino_i != destino_j): #Se forem iguais EX: (3,3) Nem precista testar.

                                    #Tratar inconssistências do tipo: Não haver uma chave 1,0 na tabela
                                    #mas haver uma 0,1. São a mesma chave, a mesma equivalência a ser tratada

                                    if (chave_destino not in tabela_equivalencia): #Caso ocorra inverte-se a chave
                                        chave_destino = destino_j + "," + destino_i
                                        slot = tabela_equivalencia[chave_destino] #recebe o valor que está na tabela hash
                                    else: slot = tabela_equivalencia[chave_destino]

                                    if(slot == "X"): #Se não forem equivalentes. automaticamente os estados que estãos endo testados nnão são
                                        if(possivel_chave not in tabela_equivalencia):
                                            possivel_chave = estado_j + "," + estado_i
                                            tabela_equivalencia[possivel_chave] = "X"

                                            # Se esses estados que foram marcados agora estiverem amarrados
                                            # com outros estados. Estes também são atualizados e marcados

                                            if(possivel_chave in amarrados):
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                        else:
                                            tabela_equivalencia[possivel_chave] = "X"
                                            if (possivel_chave in amarrados):
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                    #Caso não tiverem sido marcados ainda, amarra-se.
                                    elif(slot == "N"):
                                        amarrados[chave_destino] = possivel_chave #Se eu marcar chave destino, terei que marcar possivel chave

                # Se já não forem equivalentes (final com não final) atualiza-se a tabela sem passar pelo procedimento.
                else:
                    estado_i = lista_estados[i]
                    estado_j = lista_estados[j]
                    possivel_chave = estado_i + "," + estado_j

                    if (possivel_chave not in tabela_equivalencia):
                        possivel_chave = estado_j + "," + estado_i
                        tabela_equivalencia[possivel_chave] = "X"

                    else: tabela_equivalencia[possivel_chave] = "X"

        # EQUIVALÊNCIAS MONTADAS

        keys = tabela_equivalencia.keys() #recebe as chaves da tabela

        for i in keys:
            if(tabela_equivalencia[i] == "N"): #As chaves que contiverem um N (espaço em branco) simbolizam estados equivalentes
                lista_equivalentes.append(i)

        return lista_equivalentes #retorna a lista de equivalências.

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
        n_estados = len(self.states)
        for i in range(0, n_estados):
            print(i)

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
