from Controller.AFDController import AFDController
from Model.State import State
import copy

#Contador de ID's de autômatos. (Auto Increment)
#automata_Id_counter = 0 (Passei pra classe AFDController

AF = AFDController()

entrada = input("Digite o arquivo de entrada: ")

automata = AF.load(entrada)
automata_copy = copy.deepcopy(automata) # Cópia do Objeto automata.

#automata.printAutomata()
#estados_equivalentes = AF.equivalents(automata) #Passei para a funçao de minimização

# Se eu passasse "automata" nas duas funções, a função negado iria negar o automato já minimizado,
# pois a função minimum modifica o objeto. Logo, é necessário criar uma cópia para que a função
# negado não negue o automato já minimizado, mas sim o original.
# Também passei a chamada da função SAVE pra dentro de minimum e complement. Para que possam salvar
# os automatos com mnemônicos: min (minimizado) e neg (negado).

#minimo = AF.minimum(automata, entrada)
#negado = AF.complement(automata_copy, entrada)
inicial = AF.initial(automata)
inicial.printState()

