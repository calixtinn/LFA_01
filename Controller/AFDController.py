"""
@AFDController
@author: Matheus Calixto | Samuel Terra
Classe que implementa todas as funcionalidade um Automoto Finito Deterministico.
"""
import xml.etree.ElementTree as ET
from Model.State import State
from Model.Transition import Transition
from Model.AFD import AFD

from xml.dom.minidom import Document


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
        cont_trans = 0
        for i in root.iter('transition'):
            From = i.find('from').text
            To = i.find('to').text
            Read = i.find('read').text

            # Adiciona o caractere lido na lista do alfabeto
            self.alphabet.append(Read)

            transition = Transition(cont_trans, From, To, Read)
            self.transitions.append(transition)
            cont_trans += 1
        # Fim da obtenção das informações referentes às transições.

        alphabet = list(set(self.alphabet))
        automato = AFD(AFDController.automata_Id_counter, self.states, self.transitions, s_initial, self.finals,
                       alphabet)  # Cria um automato

        AFDController.automata_Id_counter += 1

        return automato

    def save(self, automata, jffFile):
        """
        Metodo responsavel por salvar AFD em um arquivo XML em formato jff.
        :type jffFile: str
        :type automata: AFD
        :param automata
        :param jffFile
        :rtype bool
        """
        doc = Document()

        structure = doc.createElement('structure')
        type = doc.createElement('type')
        automaton = doc.createElement('automaton')

        doc.appendChild(structure)  # ponto de partida
        type.appendChild(doc.createTextNode('fa'))
        structure.appendChild(type)

        for theState in automata.getStates():
            final = doc.createElement('final')
            initial = doc.createElement('initial')

            x = doc.createElement('x')
            y = doc.createElement('y')

            x.appendChild(doc.createTextNode(theState.getPosx()))
            y.appendChild(doc.createTextNode(theState.getPosy()))

            state = doc.createElement('state')
            state.setAttribute('id', theState.getId())
            state.setAttribute('name', theState.getName())
            state.appendChild(x)
            state.appendChild(y)
            if theState.isInitial():
                state.appendChild(initial)
            if theState.isFinal():
                state.appendChild(final)

            automaton.appendChild(state)
            structure.appendChild(automaton)

        for theTransition in automata.getTransitions():
            From = doc.createElement('from')
            to = doc.createElement('to')
            read = doc.createElement('read')

            From.appendChild(doc.createTextNode(theTransition.getFrom()))
            to.appendChild(doc.createTextNode(theTransition.getTo()))
            read.appendChild(doc.createTextNode(theTransition.getRead()))

            transition = doc.createElement('transition')
            transition.appendChild(From)
            transition.appendChild(to)
            transition.appendChild(read)

            automaton.appendChild(transition)
            structure.appendChild(automaton)

        doc.writexml(open('Output/'+jffFile, 'w'), addindent='	', newl='\n', encoding='UTF-8')

        doc.unlink()

    def equivalents(self, afd):
        """
        Metodo responsavel por verificar os estados equivalentes do AFD.
        :type afd: AFD
        :param afd
        :rtype list

        """
        tabela_equivalencia = {}  # Tabela que contem a quivalência entre os estados
        lista_estados = []  # lista para o controle dos estados
        transicoes_estados = []  # transicoes dos estados
        lista_equivalentes = []  # lista de estados equivalentes
        amarrados = {}  # Dicionario contendo as amarrações entre estados no algoritmo de equivalencia.

        estados = afd.getStates()  # recebe uma lista com os estados do automato (OBJETOS)
        alfabeto = afd.getAlphabet()  # recebe uma lista contendo o alfabeto do automato
        transicoes = afd.getTransitions()  # recebe uma lista contendo as transições do autômato

        # Cria e inicializa a tabela Hash de equivalências

        for estado in estados:  # para cada estado na lista OBJETOS de estados
            lista_estados.append(estado.getId())

        n_estados = len(lista_estados)  # tamanho da lista de estados

        for i in range(0, n_estados):  # Percorre a lista de estados testando-os um a um
            e1 = lista_estados[i]
            for j in range(i + 1, n_estados):
                e2 = lista_estados[j]
                chave = e1 + "," + e2  # Cria uma chave para se testar na tabela. Ex: 1,2 (Estado1 equivalente a estado 2?)
                if (estados[i].isFinal() != estados[
                    j].isFinal()):  # Se ambos não forem finais ou não finais já não é equivalente
                    tabela_equivalencia[chave] = "X"  # Marca na tabela Hash que não é equivalente.
                else:
                    tabela_equivalencia[chave] = "N"  # Caso contrário, marca como N (Espaço vazio a ser testado)
        # CRIADA A TABELA

        # Salva em uma lista as todas as transições de todos os estados.
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
                            chave_destino = destino_i + "," + destino_j  # cria uma chave para testar na tabela

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
                                possivel_chave = estado_i + "," + estado_j  # Cria-se uma chave para marcar na tabela

                                if (destino_i != destino_j):  # Se forem iguais EX: (3,3) Nem precista testar.

                                    # Tratar inconssistências do tipo: Não haver uma chave 1,0 na tabela
                                    # mas haver uma 0,1. São a mesma chave, a mesma equivalência a ser tratada

                                    if (chave_destino not in tabela_equivalencia):  # Caso ocorra inverte-se a chave
                                        chave_destino = destino_j + "," + destino_i
                                        slot = tabela_equivalencia[
                                            chave_destino]  # recebe o valor que está na tabela hash
                                    else:
                                        slot = tabela_equivalencia[chave_destino]

                                    if (
                                                slot == "X"):  # Se não forem equivalentes. automaticamente os estados que estãos endo testados nnão são
                                        if (possivel_chave not in tabela_equivalencia):
                                            possivel_chave = estado_j + "," + estado_i
                                            tabela_equivalencia[possivel_chave] = "X"

                                            # Se esses estados que foram marcados agora estiverem amarrados
                                            # com outros estados. Estes também são atualizados e marcados

                                            if (possivel_chave in amarrados):
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                        else:
                                            tabela_equivalencia[possivel_chave] = "X"
                                            if (possivel_chave in amarrados):
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                    # Caso não tiverem sido marcados ainda, amarra-se.
                                    elif (slot == "N"):
                                        amarrados[
                                            chave_destino] = possivel_chave  # Se eu marcar chave destino, terei que marcar possivel chave

                # Se já não forem equivalentes (final com não final) atualiza-se a tabela sem passar pelo procedimento.
                else:
                    estado_i = lista_estados[i]
                    estado_j = lista_estados[j]
                    possivel_chave = estado_i + "," + estado_j

                    if (possivel_chave not in tabela_equivalencia):
                        possivel_chave = estado_j + "," + estado_i
                        tabela_equivalencia[possivel_chave] = "X"

                    else:
                        tabela_equivalencia[possivel_chave] = "X"

        # EQUIVALÊNCIAS MONTADAS

        keys = tabela_equivalencia.keys()  # recebe as chaves da tabela

        for i in keys:
            if (tabela_equivalencia[
                    i] == "N"):  # As chaves que contiverem um N (espaço em branco) simbolizam estados equivalentes
                lista_equivalentes.append(i)

        return lista_equivalentes  # retorna a lista de equivalências.

    def minimum(self, afd, jffin):
        """
        Metodo responsavel por realizar a minimização do AFD.
        :param AFD
        :param jff_entrada
        :rtype AFD
        """

        transicoes = afd.getTransitions()
        equivalentes = self.equivalents(afd)

        # Para cada equivalência encontrada na lista de equivalências, realiza-se a modificação
        # nos estados e transições. Por convenção, vai-se deletar o primeiro estado da equivalência. Ex:
        # Equivalência 1,3 - > Deleta-se o 1.

        for i in equivalentes:
            aux = i.split(',')
            e1 = aux[0]
            e2 = aux[1]

            # Para cada transição, sempre que To for o e1, ou seja,
            # sempre que estiver jogando algo em e1,  passa-se a jogar em e2
            # Se for um looping, ex: From 1 To 1 Read a,  modifica-se também o From.

            for t in transicoes:

                if (t.getTo() == t.getFrom() and t.getTo() == e1):
                    t.setTo(e2)
                    t.setFrom(e2)
                elif (t.getTo() == e1):
                    t.setTo(e2)
                elif (t.getFrom() == e1):
                    t.setFrom(e2)

        min_transicoes = transicoes[:] #Lista auxiliar para deletar transições repetidas

        #Varre a lista de transições modificadas para eliminar transições repetidas

        for i in range(0, len(transicoes)):
            from_i = transicoes[i].getFrom()
            to_i = transicoes[i].getTo()
            read_i = transicoes[i].getRead()
            for j in range(i + 1, len(transicoes)):
                from_j = transicoes[j].getFrom()
                to_j = transicoes[j].getTo()
                read_j = transicoes[j].getRead()
                if (from_i == from_j and to_i == to_j and read_i == read_j):
                    del min_transicoes[j]

        transicoes = min_transicoes[:]
        afd.setTransitions(transicoes) #Seta no automato sua nova lista de transições

        #Transições eliminadas

        #Eliminar estados:

        for e in equivalentes:
            aux = e.split(',')
            e1 = aux[0]
            self.deleteState(afd, e1)

        jffout = "min_" + jffin
        self.save(afd, jffout)

        return afd

    def equivalent(self, m1, m2):
        """
        Metodo responsavel por verificar a equivalencia de dois AFDs.
        :param m1
        :param m2
        :rtype bool
        """
        pass

    def complement(self, automata, jffin):
        """
        Metodo responsavel por realizar o complemento AFD.
        :type automata: AFD
        :type jffin: String
        :rtype AFD
        """
        stateList = automata.getStates()

        for theState in stateList:
            if theState.isFinal():
                theState.setFinal(False)
            else:
                theState.setFinal(True)

        jffout = "neg_" + jffin
        self.save(automata, jffout)

        return automata

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

    def initial(self, afd):
        """
        Metodo responsavel por retornar o estado inicial do AFD.
        :rtype State
        """
        id = afd.getInitial()
        estados = afd.getStates()

        for e in estados:
            if(id == e.getId()):
                inicial = e
                break

        return inicial

    def move(self):
        """
        xxxxxxx
        :rtype 
        """
        pass

    def final(self, afd):
        """
        Metodo responsavel por retornar os estados finais do AFD.
        :rtype State
        """
        lista_ids = afd.getFinals()
        estados = afd.getStates()
        lista_finais = []

        for e in estados:
            if(e.getId() in lista_ids):
                lista_finais.append(e)

        return lista_finais

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

    def deleteState(self, afd, id):
        """
        Metodo responsavel por deletar um estado do AFD.
        :param id
        :rtype list
        """
        estados = afd.getStates()

        for e in estados:
            if(e.getId() == id):
                del_state = e
                break

        index = estados.index(del_state)

        del estados[index]

    def deleteTransition(self, transitions, source, target, consume):
        """
        Metodo responsavel por deletar uma transição de um estado a outro.
        :param source
        :param target
        :param consume
        :rtype list
        """