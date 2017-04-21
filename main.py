import xml.etree.ElementTree as ET
from Model.State import State

doc = ET.parse('Input/a_b_impar.jff')

# recupera a tag principal
root = doc.getroot()


def le_jff(doc, root, transicoes):

    # listar a galera

    # Iterando na tag <state>
    for i in root.iter('state'):

        x = i.find('x').text
        y = i.find('y').text
        print('Estado: ' + i.attrib['name'])
        print('ID: ' + i.attrib['id'])
        print('X: ' + x)
        print('Y: ' + y)
        if (i.find('initial') != None):
            print("INICIAL!")
        if (i.find('final') != None):
            print("FINAL!")
        print("Transicoes: " + str(transicoes[int(i.attrib['id'])]))
        print('*' * 10)

def le_transicoes(transicoes, doc, root):

    # listar a galera

    # Iterando na tag <transition>
    for i in root.iter('transition'):

        fonte = i.find('from').text
        destino = i.find('to').text
        caractere = i.find('read').text

        transicoes[int(fonte)].append([fonte + "," + destino +"," + caractere])

    return transicoes

def qtde_estados(doc, root):

    cont = 0
    for i in root.iter('state'):
        cont += 1
    return cont

n_estados = qtde_estados(doc, root)
transicoes = []

for i in range(0,(n_estados)):
    transicoes.append([])

transicoes = le_transicoes(transicoes, doc, root)

#le_jff(doc, root, transicoes)

q1 = State(0,"q1",False,True)

print("Nome do Estado: " + q1.getName())


