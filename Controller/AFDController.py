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

    def load(self, jffFile, cont):
        """
        Este metodo é responsavel por ler um arquivo XML em formato jff contendo o AFD.
        :return @AFD
        """
        states = []                         # Lista de estados
        transitions = []                    # Lista de transições
        finals = []                         # Lista de estados finais
        s_initial = ""                      # Guardará o ID do estado inicial
        doc = ET.parse("Input/" + jffFile)  # Recebendo o arquivo de entrada via parametro da função.
        root = doc.getroot()                # Recebendo a tag root
        alphabet = []                       # alfabeto que o automato suporta

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
        for i in root.iter('transition'):
            From = i.find('from').text
            To = i.find('to').text
            Read = i.find('read').text

            # Adiciona o caractere lido na lista do alfabeto
            alphabet.append(Read)

            transition = Transition(From, To, Read)
            transitions.append(transition)
        # Fim da obtenção das informações referentes às transições.

        alphabet = list(set(alphabet))
        automato = AFD(cont, states, transitions, s_initial, finals, alphabet) #Cria um automato

        return automato
