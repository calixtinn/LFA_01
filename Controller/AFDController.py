"""
Classe AFDController
@author: Matheus Calixto | Samuel Terra

Classe que implementa todas as funcionalidades de um Automoto Finito Deterministico.
"""
import xml.etree.ElementTree as ET
from Model.State import State
from Model.Transition import Transition
from Model.AFD import AFD
from xml.dom.minidom import Document


class AFDController(object):
    """
    Classe que implementa todas as funcionalidade um Automoto Finito Deterministico.
    """

    def load(self, jffFile):
        """
        Metodo responsavel por ler um arquivo XML em formato jff conteudo o AFD. 
        :return: Retorna uma instancia criada de um AFD
        :rtype: AFD
        :param jffFile
        :rtype AFD
        """
        states = []  # Lista de estados
        transitions = []  # Lista de transições
        finals = []  # Lista de estados finais
        alphabet = []  # alfabeto que o automato suporta

        # Guardará o ID do estado inicial
        s_initial = ""
        # Recebendo o arquivo de entrada via parametro da função.
        # Não tem prefixo porque agora irá pegar dinamicamento no sistema operacional
        doc = ET.parse(jffFile)
        root = doc.getroot()  # Recebendo a tag root

        # iterando em cada tag State para pegar as informações
        for i in root.iter('state'):

            x = i.find('x').text
            y = i.find('y').text
            name = i.attrib['name']
            id = i.attrib['id']

            # Se nesse estado houver a tag inicial, seta o estado como inicial.
            if i.find('initial') is not None:
                initial = True
                s_initial = id
            else:
                initial = False

            # Se nesse estado houver a tag final, seta o estado como final.
            if i.find('final') is not None:
                final = True
                finals.append(id)
            else:
                final = False

            # Cria um objeto Estado
            state = State(id, name, x, y, initial, final)

            # Adiciona na lista de estados
            states.append(state)

        # Fim da obtenção das informações referentes aos estados

        # Iterando na tag <transition>
        # Pegando as transições
        cont_trans = 0
        for i in root.iter('transition'):
            From = i.find('from').text
            To = i.find('to').text
            Read = i.find('read').text

            if Read is None:  # Trata o movimento vazio, representado pelo caractere §
                Read = '§'

            # Adiciona o caractere lido na lista do alfabeto
            alphabet.append(Read)

            transition = Transition(cont_trans, From, To, Read)
            transitions.append(transition)
            cont_trans += 1
        # Fim da obtenção das informações referentes às transições.

        alphabet = list(set(alphabet))
        automato = AFD(states, transitions, s_initial, finals,
                       alphabet)  # Cria um automato

        return automato

    def save(self, automata, jffFile):
        """
        Metodo responsavel por salvar AFD em um arquivo XML em formato jff.
        :type jffFile: str
        :type automata: AFD
        :param automata
        :param jffFile
        """
        # Cria um documento (root) Dom para gerar o xml
        doc = Document()

        # Cria tag 'structure' para o xml
        structure = doc.createElement('structure')
        # Cria tag 'type' para o xml
        type = doc.createElement('type')
        # Cria tag 'automaton' para o xml
        automaton = doc.createElement('automaton')

        # adiciona a tag 'structure' na raiz do documento xml
        doc.appendChild(structure)
        # adiciona o texto 'fa' dentro da tag 'type'
        type.appendChild(doc.createTextNode('fa'))
        # Adiciona a tag 'type' dentro da tag 'structure'
        structure.appendChild(type)

        # Cria a estrutura xml de todos os estados
        for theState in automata.getStates():
            # Cria tag 'final'
            final = doc.createElement('final')
            # Cria tag 'initial'
            initial = doc.createElement('initial')

            # Cria tag da coordenada 'x'
            x = doc.createElement('x')
            # Cria tag da coordenada 'y'
            y = doc.createElement('y')

            # Busca o valor da coordenada x do estado e adiciona dentro da sua tag
            x.appendChild(doc.createTextNode(theState.getPosx()))
            # Busca o valor da coordenada y do estado e adiciona dentro da sua tag
            y.appendChild(doc.createTextNode(theState.getPosy()))

            # Cria a tag 'state'
            state = doc.createElement('state')
            # Seta os atributos 'id' e 'name'
            state.setAttribute('id', theState.getId())
            state.setAttribute('name', theState.getName())
            # Adiciona as duas coordenadas dentro do estado
            state.appendChild(x)
            state.appendChild(y)
            # Se o estado for final ou inicial, adiciona a respectiva tag
            if theState.isInitial():
                state.appendChild(initial)
            if theState.isFinal():
                state.appendChild(final)

            # Adiciona o estado no automato
            automaton.appendChild(state)
            # Adiciona o 'automaton' na 'structure'
            structure.appendChild(automaton)

        # Cria toda a estrutura xml das transicoes
        for theTransition in automata.getTransitions():
            # Cria as tags necessarias da 'transition'
            From = doc.createElement('from')
            to = doc.createElement('to')
            read = doc.createElement('read')

            # Adiciona valores nas tag
            From.appendChild(doc.createTextNode(theTransition.getFrom()))
            to.appendChild(doc.createTextNode(theTransition.getTo()))
            read.appendChild(doc.createTextNode(theTransition.getRead()))

            # Cria uma tag 'transition'
            transition = doc.createElement('transition')
            # Adiciona as tag criadas dentro da tag transition
            transition.appendChild(From)
            transition.appendChild(to)
            transition.appendChild(read)

            # Adiciona a 'transition' dentro do 'automaton'
            automaton.appendChild(transition)
            # Adiciona o 'automaton' dentro da 'structure'
            structure.appendChild(automaton)

        # Gera o arquivo de saida com algumas confuracoes do arquivo (identacao, nova linha, codificacao)
        doc.writexml(open(jffFile, 'w'), addindent='	', newl='\n', encoding='UTF-8')

        # Libera memoria
        doc.unlink()

    def equivalent_states(self, afd):
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
                if i.getFrom() == lista_estados[j]:
                    transicoes_estados.append(i)

        for i in range(0, n_estados):  # Percorre a lista de estados
            trans_i = {}  # transicoes de i (dicionario)
            for k in transicoes_estados:  # procura as transições dos respectivos estados
                if k.getFrom() == lista_estados[i]:
                    trans_i[k.getRead()] = k.getTo()  # Ex: ["a"] = 1 [caractere] = para onde vai.
            # End pegar transições de I

            for j in range(i + 1, n_estados):  # Segundo for para percorrer a lista e testar um a um

                # Os estados precisam ser iguais (final e final) ou (não final e não final) para testar
                # Se não forem, quer dizer que eles já não são equivalentes e não precisa-se testar.

                if estados[i].isFinal() == estados[j].isFinal():

                    trans_j = {}  # transicoes de j (dicionario)
                    for k in transicoes_estados:  # procura as transições dos respectivos estados
                        if k.getFrom() == lista_estados[j]:
                            trans_j[k.getRead()] = k.getTo()
                    # End pegar transições de j

                    for a in alfabeto:  # Para cada caracter do alfabeto...

                        if a in trans_i and a in trans_j:   # Se houver transições com o caractere do alfabeto em
                                                            # ambos os estados.

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
                            if destino_i != lista_estados[j]:

                                estado_i = lista_estados[i]
                                estado_j = lista_estados[j]
                                possivel_chave = estado_i + "," + estado_j  # Cria-se uma chave para marcar na tabela

                                if destino_i != destino_j:  # Se forem iguais EX: (3,3) Nem precista testar.

                                    # Tratar inconssistências do tipo: Não haver uma chave 1,0 na tabela
                                    # mas haver uma 0,1. São a mesma chave, a mesma equivalência a ser tratada

                                    if chave_destino not in tabela_equivalencia:  # Caso ocorra inverte-se a chave
                                        chave_destino = destino_j + "," + destino_i
                                        slot = tabela_equivalencia[
                                            chave_destino]  # recebe o valor que está na tabela hash
                                    else:
                                        slot = tabela_equivalencia[chave_destino]

                                    # Se não forem equivalentes. automaticamente os estados que estãos endo testados nnão são
                                    if slot == "X":
                                        if possivel_chave not in tabela_equivalencia:
                                            possivel_chave = estado_j + "," + estado_i
                                            tabela_equivalencia[possivel_chave] = "X"

                                            # Se esses estados que foram marcados agora estiverem amarrados
                                            # com outros estados. Estes também são atualizados e marcados

                                            if possivel_chave in amarrados:
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                        else:
                                            tabela_equivalencia[possivel_chave] = "X"
                                            if possivel_chave in amarrados:
                                                atualizar = amarrados[possivel_chave]
                                                tabela_equivalencia[atualizar] = "X"
                                    # Caso não tiverem sido marcados ainda, amarra-se.
                                    elif slot == "N":
                                        # Se eu marcar chave destino, terei que marcar possivel chave
                                        amarrados[chave_destino] = possivel_chave

                # Se já não forem equivalentes (final com não final) atualiza-se a tabela sem passar pelo procedimento.
                else:
                    estado_i = lista_estados[i]
                    estado_j = lista_estados[j]
                    possivel_chave = estado_i + "," + estado_j

                    if possivel_chave not in tabela_equivalencia:
                        possivel_chave = estado_j + "," + estado_i
                        tabela_equivalencia[possivel_chave] = "X"

                    else:
                        tabela_equivalencia[possivel_chave] = "X"

        # EQUIVALÊNCIAS MONTADAS

        keys = tabela_equivalencia.keys()  # recebe as chaves da tabela

        for i in keys:
            # As chaves que contiverem um N (espaço em branco) simbolizam estados equivalentes
            if tabela_equivalencia[i] == "N":
                lista_equivalentes.append(i)

        return lista_equivalentes  # retorna a lista de equivalências.

    def minimum(self, afd):
        """
        Metodo responsavel por realizar a minimização do AFD.
        :param afd
        :rtype AFD
        """

        transicoes = afd.getTransitions()
        equivalentes = self.equivalent_states(afd)
        inicial = afd.getInitial()
        transicoes_iguais = []

        # Para cada equivalência encontrada na lista de equivalências, realiza-se a modificação
        # nos estados e transições. Por convenção, vai-se deletar o primeiro estado da equivalência. Ex:
        # Equivalência 1,3 - > Deleta-se o 1.

        for i in equivalentes:
            aux = i.split(',')
            e1 = aux[0]
            e2 = aux[1]

            # Não elimino o inicial, caso ele for o candidato da eliminação.
            if e1 == inicial:
                aux = e1
                e1 = e2
                e2 = aux

            # Para cada transição, sempre que To for o e1, ou seja,
            # sempre que estiver jogando algo em e1,  passa-se a jogar em e2
            # Se for um looping, ex: From 1 To 1 Read a,  modifica-se também o From.

            for t in transicoes:
                if t.getTo() == t.getFrom() and t.getTo() == e1:
                    t.setTo(e2)
                    t.setFrom(e2)
                elif t.getTo() == e1:
                    t.setTo(e2)
                elif t.getFrom() == e1:
                    t.setFrom(e2)

        min_transicoes = transicoes[:]  # Lista auxiliar para deletar transições repetidas

        # Varre a lista de transições modificadas para eliminar transições repetidas

        for i in range(0, len(transicoes)):
            from_i = transicoes[i].getFrom()
            to_i = transicoes[i].getTo()
            read_i = transicoes[i].getRead()
            for j in range(i + 1, len(transicoes)):
                from_j = transicoes[j].getFrom()
                to_j = transicoes[j].getTo()
                read_j = transicoes[j].getRead()
                if from_i == from_j and to_i == to_j and read_i == read_j:
                    # del min_transicoes[j]
                    transicoes_iguais.append(int(transicoes[j].getId()))

        transicoes_iguais.sort(reverse=True)

        for t in transicoes_iguais:
            del min_transicoes[t]

        transicoes = min_transicoes[:]
        afd.setTransitions(transicoes)  # Seta no automato sua nova lista de transições

        # Transições eliminadas

        # Eliminar estados:

        for e in equivalentes:
            aux = e.split(',')
            e1 = aux[0]
            e2 = aux[1]
            # Não elimino o inicial, caso ele for o candidato da eliminação.
            if e1 == inicial:
                aux = e1
                e1 = e2
                e2 = aux
            mensagem = self.deleteState(afd, e1)

        return afd

    def complement(self, automata):
        """
        Metodo responsavel por realizar o complemento AFD.
        :type automata: AFD
        :rtype AFD
        """
        stateList = automata.getStates()
        final_list = []

        for theState in stateList:
            if theState.isFinal():
                theState.setFinal(False)
            else:
                theState.setFinal(True)
                final_list.append(theState)

        automata.setStates(stateList, final_list)

        return automata

    def equivalent_automatas(self, automata1, automata2):
        """
        Metodo responsavel por verificar a equivalencia de dois AFDs.
        :param automata1: AFD
        :param automata2: AFD
        :rtype string
        """
        '''
        dois automotos são quivalentes, se o minimo de ambos forem iguais
        verificar se o primeiro estado dos dois automatos são equivalentes
        tem que ser iguais depois da minimizacao:
            o alfabeto
            quantidade de estados
            estado inicial
        '''
        min_m1 = self.minimum(automata1)
        min_m2 = self.minimum(automata2)

        n_estados_m1 = len(min_m1.getStates())
        n_estados_m2 = len(min_m2.getStates())
        n_transicoes_m1 = len(min_m1.getTransitions())

        if min_m1.getAlphabet() != min_m2.getAlphabet():
            mensagem = "O alfabeto dos dois AFD's são diferentes. Logo, NÃO são equivalentes"
            return mensagem
        elif n_estados_m1 != n_estados_m2:
            mensagem = "A quantaide de estados dos dois AFD's são diferentes. Logo NÃO são equivalentes"
            return mensagem
        else:
            # Roda o algoritmo de equivalencia para saber se os estados inicias são equivalentes.
            # Para tal, cria-se um novo AFD contendo todos os estados dois dois AFD's
            # Executa-se o algoritmo como se os dois autômatos fossem um só!

            estados_min1 = min_m1.getStates()
            estados_min2 = min_m2.getStates()

            transicoes_min1 = min_m1.getTransitions()
            transicoes_min2 = min_m2.getTransitions()

            inicial_min1 = str(min_m1.getInitial())
            estados_finais = min_m1.getFinals()
            alfabeto = min_m1.getAlphabet()

            # Renomea os Id's dos estados de min2 a partir do numero de estados de min1
            # Ex: se min1 tem 2 estados (ID's: 0 e 1). O contador de ID's dos estados de min2 começará
            # com ID 2, e assim por diante.

            id_cont = n_estados_m1

            for e in estados_min2:
                e.setId(str(id_cont))
                id_cont += 1
                if e.isFinal():
                    estados_finais.append(
                        str(e.getId()))  # Adiciona na lista de estados finais, os estados finais do AFD2
                if e.isInitial():
                    inicial_min2 = e.getId()  # Pega o estado inicial do AFD2, com o ID já modificado

            # Mesma ideia para os ID's das transições.

            id_cont = n_transicoes_m1

            for t in transicoes_min2:
                old_from = int(t.getFrom())  # Recebe o ID antigo do estado fonte
                old_to = int(t.getTo())  # Recebe o ID antigo do estado destino
                t.setId(str(id_cont))  # Altera o ID com base no contador atual
                id_cont += 1  # Incrementa o contador
                t.setFrom(str(old_from + n_estados_m1))  # Atualiza o novo ID do estado fonte
                t.setTo(str(old_to + n_estados_m1))     # Atualiza o novo ID do estado destino

            novos_estados = estados_min1 + estados_min2  # Nova lista de estados
            novas_transicoes = transicoes_min1 + transicoes_min2  # Nova lista de transições

            novo_afd = AFD(novos_estados, novas_transicoes, inicial_min1, estados_finais, alfabeto)  # Novo AFD.
            estados_equivalentes = self.equivalent_states(novo_afd)  # Verifica a equivalência de estados

            # Testa se os estados iniciais dos dois AFD's minimizados são equivalentes. Se sim, retorna true.

            for eq in estados_equivalentes:
                aux = eq.split(',')
                e1 = aux[0]
                e2 = aux[1]

                if (e1 == inicial_min1 and e2 == inicial_min2) or (e1 == inicial_min2 and e2 == inicial_min1):
                    mensagem = "\nOs Autômatos são equivalentes!"
                    return mensagem

        mensagem = "\nOs estados iniciais dos dois AFD's não são equivalentes. Logo os AFD's NÃO são equivalentes"
        return mensagem

    def union(self, m1, m2):
        """
        Metodo responsavel por realizar a união do AFD da classe com um outro.
        :param m1
        :param m2
        :rtype AFD
        """
        # Pega informações dos dois autômatos passados por parâmetro (Estados e transições)

        estados_m1 = m1.getStates()
        estados_m2 = m2.getStates()
        transicoes_m1 = m1.getTransitions()
        transicoes_m2 = m2.getTransitions()

        # O alfabeto do autômato resultante, vai ser a união dos alfabetos dos dois autômatos.

        alfabeto_uniao = set(m1.getAlphabet() + m2.getAlphabet())

        # Cria uma tabela contendo como chave o estado, e como valores suas transições!

        trans_estadosm1, trans_estadosm2 = self.tabela_transicoes(transicoes_m1, transicoes_m2)

        # Faz-se a multiplicação dos estados dos dois autômatos, criando assim uma nova lista de estados
        # Contendo um novo ID, com um novo nome (seguindo o padrão: Estado de m1 = 0, Estado de m2 = 0
        # Estado multiplicado = 0,0), as posições x e y obtidas através das médias das posições dos estados
        # de m1 e m2, e uma flag dizendo se é inicial (os dois iniciais de m1 e m2) e/ou final
        # (final de m1 com final de m2 OU final de m1 com não final de m2 e vice versa)

        estados_uniao, finais_uniao, inicial_uniao, estado_id_uniao = self.multiplica_estados(1, estados_m1, estados_m2)

        # De posse dos novos estados provindos da MULTIPLICAÇÃO dos dois AFD's, define-se as transições

        transicoes_uniao = self.monta_transicoes(estados_uniao, alfabeto_uniao, trans_estadosm1, trans_estadosm2,
                                                 estado_id_uniao)

        if inicial_uniao == "":
            print("ERRO!, não há estado inicial nesse autômato. Verifique o arquivo .jff")

        else:
            # Cria o novo afd
            afd_uniao = AFD(estados_uniao, transicoes_uniao, inicial_uniao, finais_uniao, alfabeto_uniao)
            return afd_uniao

    def monta_transicoes(self, estados, alfabeto, trans_estadosm1, trans_estadosm2, estado_id):
        """
        Método responsável por montar as transições do novo AFD, através do novo conjunto de estados,
        do novo alfabeto, das transições dos estados dos autômatos m1 e m2, e da tabela de transições
        de cada estado do autômato.

        :param estados:
        :param alfabeto:
        :param trans_estadosm1:
        :param trans_estadosm2:
        :param estado_id:
        :return: novas_transicoes:
        """

        novas_transicoes = []  # Lista contendo as novas transições do AFD resultante.
        id_transicao = 0  # inicializa o contador do ID das transições

        # Para cada estado do AFD resultante, faz-se a separação dos estados em e1 e e2
        # Para que sejam definidas, para cada letra do alfabeto, os destinos de e1 e e2.
        # Depois de definidos, define-se a transição com base nos ID's da tabela montada anteriormente.

        for e in estados:
            nome_estado = e.getName().split(",")  # Ex: Estado (0,0) -> e1 = 0, e2 = 0.
            e1 = nome_estado[0]
            e2 = nome_estado[1]

            trans_e1 = trans_estadosm1[e1]  # Transições estado e1
            trans_e2 = trans_estadosm2[e2]  # Transições estado e2

            for letra in alfabeto:
                destino_e1 = self.monta_destino(e1, trans_e1, letra)
                destino_e2 = self.monta_destino(e2, trans_e2, letra)

                novo_destino = destino_e1 + ',' + destino_e2  # Ex (1,3) Estado 1 e estado 3.

                novo_destino = estado_id[novo_destino]  # Verifica-se na tabela qual o ID desse estado (1,3)

                nova_transicao = Transition(id_transicao, e.getId(), novo_destino, letra)  # Cria a transição.
                novas_transicoes.append(nova_transicao)
                id_transicao += 1

        return novas_transicoes

    def tabela_transicoes(self, transicoes_m1, transicoes_m2):

        """
        Método responsável por criar e retornar as tabelas e transições de cada estado.
        Chave = ID do estado
        Valor = Transições
        Exemplo: Tabela de transições do estado 0:

        0 = [1,b; 0,a; 3,c]

        ID do estado = Lista de transições (estado destino, caractere lido)

        :param transicoes_m1:
        :param transicoes_m2:
        :return: trans_estadosm1, trans_estadosm2
        """

        trans_estadosm1 = {}  # Tabelas de transições dos estados de m1
        trans_estadosm2 = {}  # Tabelas de transições dos estados de m2

        for t in transicoes_m1:
            estado = t.getFrom()
            valor = []

            # Se a lista de transições estiver vazia, adiciona-se uma nova chave com uma nova lista

            if (trans_estadosm1.get(estado) == None):
                valor.append(t.getTo() + ',' + t.getRead())
                trans_estadosm1[estado] = valor

            # Caso já hajam elementos na lista de transições, não cria-se uma outra chave, mas sim
            # atualiza a lista de transições da chave existente.

            else:
                valor = trans_estadosm1[estado]
                valor.append(t.getTo() + ',' + t.getRead())

        for t in transicoes_m2:
            estado = t.getFrom()
            valor = []

            if trans_estadosm2.get(estado) is None:
                valor.append(t.getTo() + ',' + t.getRead())
                trans_estadosm2[estado] = valor
            else:
                valor = trans_estadosm2[estado]
                valor.append(t.getTo() + ',' + t.getRead())

        return trans_estadosm1, trans_estadosm2

    def multiplica_estados(self, tipo, estados_m1, estados_m2):

        """
        Método que realiza a multiplicação dos estados dois dois autômatos, para que as operações
        de união e intercessão sejam realizadas.
        Essa operaçõo ocorre multiplicando cada estado de m1 por cada estado de m2.
        Ex: Autômato 1 = Estados 0 e 1
            Autômato 2 = Estados 0, 1 e 2

        A multipliação terá como resultado 6 estados (2 x 3):
        0,0 - 0,1 - 0,2 - 1,0 - 1,1 - 1,2

        O método retorna a lista com os novos estados, a lista de estados finais baseada na operação
        realizada (união ou intercessão), o estado inicial e a lista de estados e ID's (tabela hash)

        :param tipo:
        :param estados_m1:
        :param estados_m2:
        :return:
        """

        estados_finais = []
        novos_estados = []

        estado_inicial = ""
        id_estado = 0

        estado_id = {}

        for s1 in estados_m1:
            id_1 = s1.getId()
            for s2 in estados_m2:
                id_2 = s2.getId()
                novo_nome = id_1 + "," + id_2
                novo_x = (float(s1.getPosx()) + float(s2.getPosx())) / 2
                novo_y = (float(s1.getPosy()) + float(s2.getPosy())) / 2
                if tipo == 1:  # união
                    if s1.isFinal() or s2.isFinal():
                        final = True
                        estados_finais.append(novo_nome)
                    else:
                        final = False
                elif tipo == 0:  # Intercessão
                    if s1.isFinal() and s2.isFinal():
                        final = True
                        estados_finais.append(novo_nome)
                    else:
                        final = False
                if s1.isInitial() and s2.isInitial():
                    initial = True
                    estado_inicial = novo_nome
                else:
                    initial = False
                novo_estado = State(str(id_estado), novo_nome, str(novo_x), str(novo_y), initial, final)
                novos_estados.append(novo_estado)
                estado_id[novo_nome] = str(
                    id_estado)  # Associando cada novo estado ao seu ID para definir as transições
                id_estado += 1

        return novos_estados, estados_finais, estado_inicial, estado_id

    def monta_destino(self, estado, lista_trans, letra):

        """
        Método responsável por montar o destino de cada transição do novo AFD gerado com a
        operação de união ou com a operação de intercessão.

        :param estado: estado em questão
        :param lista_trans: lista de transições do respectivo estado
        :param letra: caractere lido.
        :return: estado destino
        """

        for trans in lista_trans:  # Para cada transição do estado
            elem = trans.split(',')
            destino = elem[0]
            simbolo = elem[1]

            # Se há uma transição, lendo esta letra passada por parâmetro,
            # retorna-se o destino. Caso contrário, o estado não se movimenta, permanece nele mesmo.

            if simbolo == letra: return destino

        return estado

    def intersection(self, m1, m2):
        """
        Metodo responsavel por realizar a interseção de dois AFDs.
        :param m1
        :param m2
        :rtype AFD
        """

        # Pega informações dos dois autômatos passados por parâmetro.

        estados_m1 = m1.getStates()
        estados_m2 = m2.getStates()
        transicoes_m1 = m1.getTransitions()
        transicoes_m2 = m2.getTransitions()

        alfabeto_intercessao = set(m1.getAlphabet() + m2.getAlphabet())  # Alfabeto deste autômato

        # Cria uma tabela contendo como chave o estado, e como valores suas transições!
        trans_estadosm1, trans_estadosm2 = self.tabela_transicoes(transicoes_m1, transicoes_m2)

        # Faz-se a multiplicação dos estados dos dois autômatos, criando assim uma nova lista de estados
        # Contendo um novo ID, com um novo nome (seguindo o padrão: Estado de m1 = 0, Estado de m2 = 0
        # Estado multiplicado = 0,0), as posições x e y obtidas através das médias das posições dos estados
        # de m1 e m2, e uma flag dizendo se é inicial (os dois iniciais de m1 e m2) e/ou final
        # (final de m1 com final de m2 OU final de m1 com não final de m2 e vice versa)

        estados_intercessao, finais_intercessao, inicial_intercessao, estado_id_intercessao = self.multiplica_estados(0,
                                                                                                                      estados_m1,
                                                                                                                      estados_m2)

        # De posse dos novos estados provindos da MULTIPLICAÇÃO dos dois AFD's, define-se as transições

        transicoes_uniao = self.monta_transicoes(estados_intercessao, alfabeto_intercessao, trans_estadosm1,
                                                 trans_estadosm2,
                                                 estado_id_intercessao)

        if inicial_intercessao == "":
            print("ERRO!, não há estado inicial nesse autômato. Verifique o arquivo .jff")

        else:
            afd_intercessao = AFD(estados_intercessao, transicoes_uniao, inicial_intercessao, finais_intercessao,
                                  alfabeto_intercessao)  # Cria o novo afd
            return afd_intercessao

    def difference(self, m1, m2):
        """
        Metodo responsavel por realizar a diferença de dois AFDs.
        A diferenca pode ser feita do complemento de m1 em intercessao com m2
        Return -> m1 ∩ ¬m2.
        
        :param m1
        :param m2
        :rtype AFD
        """
        return self.intersection(m1, self.complement(m2))

    def accept(self, afd, word):
        """
        Metodo responsavel por verificar se uma determinada palavra é aceita pelo AFD.
        :param afd
        :param word
        :rtype boolean
        """

        inicial = afd.getInitial()

        return self.move(afd, inicial, word)

    def initial(self, afd):
        """
        Metodo responsavel por retornar o estado inicial do AFD.
        :rtype State
        """
        id = afd.getInitial()
        estados = afd.getStates()
        # Inicializa a variavel
        inicial = False

        for e in estados:
            if id == e.getId():
                inicial = e
                break

        return inicial

    def move(self, afd, id, word):
        """
        Método responsável por testar um movimento a partir de um estado e retornar se aceita ou não
        :param afd
        :param id
        :param word (palavra)
        
        """

        transicoes = afd.getTransitions()  # Pega a lista de transições do AFD
        estados = afd.getStates()
        comprimento_palavra = len(word)  # Pega o comprimento da palavra passada por parâmtro
        estados_finais = afd.getFinals()  # Pega a lista de estados finais do AFD
        id = str(id)  # Converte o ID em string
        existe = False
        erro = 0

        # Testa primeiro se o estado existe antes de deletá-lo
        for e in estados:
            if e.getId() == id:
                existe = True
                break

        if not existe:
            print("ERRO! Estado inexistente!")
        else:  # Se existir, segue o algoritmo para percorrer o AFD

            for i in range(0, comprimento_palavra):  # Varre toda a palavra caractere por caractere
                if not existe:  # Se não houve nenhuma transição com o estado e caractere passado, erro.
                    erro = 1
                    break
                # Percorre todas as transições procurando a transição entre o caractere da palavra e o estado passado
                for t in transicoes:
                    if t.getFrom() == id and t.getRead() == word[i]:  # se for o estado desejado e o caractere desejado
                        id = t.getTo()  # movo para o próximo estado
                        existe = True
                        break
                    else:
                        existe = False

            if erro == 1:  # Erro para não existência de transição e/ou estado
                print("Palavra REJEITADA! Estado (" + id + ") não possui transição lendo o caractere " + word[i])
            else:
                if id in estados_finais:  # Se parou em um estado final, aceita
                    print("Palavra ACEITA! Parou no estado (" + id + ")")
                else:  # Se não, rejeita.
                    print("Palavra REJEITADA! Parou no estado (" + id + ")")


    def final(self, afd):
        """
        Metodo responsavel por retornar os estados finais do AFD.
        :rtype List
        """

        idEstadosFinais = afd.getFinals()
        estadosAfd = afd.getStates()
        nomesEstadosFinais = []

        for e in estadosAfd:
            if e.getId() in idEstadosFinais:
                nomesEstadosFinais.append(e.getName())

        return nomesEstadosFinais

    def addState(self, afd, name, initial, final):
        """
        Metodo responsavel por adicionar estado ao AFD.
        :param afd
        :param name
        :param initial
        :param final
        """
        # O novo estado sempre tera o ID referente à quantidade de estados.
        # Ex: Se houverem 5 estados, significa que já há id's de 0-4. Logo
        # o próximo id disponível será = 5.

        estados = afd.getStates()
        finais = afd.getFinals()
        id = str(len(estados))
        erro = 0

        # Verifica a tentativa de adicionar mais um estado inicial no AFD, o que não é permitido.

        if initial and afd.getInitial() != None:
            print("ERRO! O autômato já possui um estado inicial! Impossível adicionar este estado.")
            return afd

        x = 0.0
        y = 0.0

        for e in estados:
            x += float(e.getPosx())
            y += float(e.getPosy())
            if name == e.getName():
                erro = 1
                break

        if erro == 1:
            print("ERRO! NOME existente!")
            return afd
        else:
            x /= len(estados)  # x = x / quantidade de estados
            y /= len(estados)
            novo_estado = State(id, name, str(x), str(y), initial, final)
            estados.append(novo_estado)
            if final:
                finais.append(id)
            print("Estado com ID = (" + id + ") adicionado com sucesso!")

        return afd

    def addTransition(self, afd, source, target, consume):
        """
        Metodo responsavel por adicionar transições ao AFD.
        :param afd
        :param source
        :param target
        :param consume
        """
        transicoes = afd.getTransitions()
        estados = afd.getStates()
        alfabeto = afd.getAlphabet()
        erro = 0
        id = str(len(transicoes))
        existe_fonte = False
        existe_destino = False

        # Testa para saber se os dois estados passados por parametro existem no AFD.

        for i in range(0, 2):
            for e in estados:
                if existe_fonte:  # Se existe o estado fonte, falta testar somente o estado destino.
                    if e.getId() == target:
                        existe_destino = True  # Se existe, sai do laço, pois já foram verificados os 2 estados.
                        break
                elif existe_destino:  # Se existe o estado de destino, falta testar somente o estado fonte
                    if e.getId() == source:
                        existe_fonte = True  # Se existe, sai do laço, pois já foram verificados os 2 estados.
                        break
                else:  # Se ainda não foi verificada a existência de nenhum estado, verifica-se.
                    if e.getId() == source:
                        existe_fonte = True
                        break

                    if e.getId() == target:
                        existe_destino = True
                        break

        if not existe_destino:
            print("ERRO! O estado de destino não existe neste autômato!")
            return afd
        elif not existe_fonte:
            print("ERRO! O estado fonte não existe neste autômato!")
            return afd
        else:  # Caso os dois estados existam, verifica-se se a transição já existe antes de adiconá-la.

            for t in transicoes:
                # Testa se a transição já existe
                if t.getFrom() == source and t.getTo() == target and t.getRead() == consume:
                    erro = 1
                    break

            if erro == 1:
                print("ERRO! Transição já existente!")
                return afd
            else:  # Se não existir, adiciona-a à lista de transições do AFD.

                nova_transicao = Transition(id, source, target, consume)
                transicoes.append(nova_transicao)
                if consume not in alfabeto:
                    alfabeto.append(consume)
                print("Transição com ID = (" + id + ") adicionada com sucesso!")
                return afd

    def deleteState(self, afd, id):
        """
        Metodo responsavel por deletar um estado do AFD.
        :param id
        :rtype string
        """
        estados = afd.getStates()
        finais = afd.getFinals()
        existe = False

        # Testa primeiro se o estado existe antes de deletá-lo
        for e in estados:
            if e.getId() == id:
                existe = True
                break

        if not existe:
            print("ERRO! Estado inexistente!")
            return afd

        else:  # Se existir, deleta-o
            for e in estados:
                if e.getId() == id:
                    del_state = e
                    break

            index = estados.index(del_state)

            del estados[index]
            if id in finais:
                index = finais.index(id)
                del finais[index]
            print("Estado de ID = (" + id + ") deletado com sucesso!")
            return afd

    def deleteTransition(self, afd, source, target, consume):
        """
        Metodo responsavel por deletar uma transição de um estado a outro.
        :param afd
        :param source
        :param target
        :param consume
        """
        transicoes = afd.getTransitions()
        existe = False

        for t in transicoes:
            if t.getFrom() == source and t.getTo() == target and t.getRead() == consume:
                del_transition = t
                existe = True
                break

        if existe:  # Se a transição existe, deleta.
            index = transicoes.index(del_transition)
            del transicoes[index]
            print("Transição de ID = (" + str(index) + ") deletada com sucesso!")
            return afd
        # Se não, retorna erro!
        else:
            print("ERRO! Esta transição não existe neste AFD!")
            return afd
