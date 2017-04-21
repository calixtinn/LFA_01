import xml.etree.ElementTree as ET
from Model.State import State
from Model.Transition import Transition
from Model.AFD import AFD

automata_Id_counter = 0 #Contador de ID's de autômatos. (Auto Increment)

def load(jffFile, cont): #Carrega o arquivo jff e RETORNA UM OBJETO DO TIPO AFD!!!!!

    states = []  # Lista de estados
    transitions = []  # Lista de transições
    finals = []  # Lista de estados finais
    s_initial = "" # Guardará o ID do estado inicial
    doc = ET.parse("Input/" + jffFile)  # Recebendo o arquivo de entrada via parametro da função.
    root = doc.getroot()  # Recebendo a tag root

    for i in root.iter('state'):  # iterando em cada tag State para pegar as informações

        x = i.find('x').text
        y = i.find('y').text
        name = i.attrib['name']
        id = i.attrib['id']

        if (i.find('initial') != None):  # Se nesse estado houver a tag inicial, seta o estado como inicial.
            initial = True
            s_initial = id
        else:
            initial = False

        if (i.find('final') != None):  # Se nesse estado houver a tag final, seta o estado como final.
            final = True
            finals.append(id)
        else:
            final = False

        state = State(id, name, x, y, initial, final) # Cria um objeto Estado

        states.append(state) #Adiciona na lista de estados

    # Fim da obtenção das informações referentes aos estados

    # Iterando na tag <transition>

    for i in root.iter('transition'): #Pegando as transições

        From = i.find('from').text
        To = i.find('to').text
        Read = i.find('read').text

        transition = Transition(From, To, Read)
        transitions.append(transition)
    # Fim da obtenção das informações referentes às transições.

    automato = AFD(cont, states, transitions, s_initial, finals) #Cria um automato

    return automato
#Fim load jff

automata = load("a_b_impar.jff", automata_Id_counter)
automata_Id_counter += 1
automata.printAutomata()