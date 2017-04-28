from Controller.AFDController import AFDController
from Model.State import State
from Model.Transition import Transition
import copy

AF = AFDController()

#entrada = input("Digite o arquivo de entrada: ")
entrada = "equivalente_1.jff"
automata = AF.load(entrada)
#automata_copy = copy.deepcopy(automata) # Cópia do Objeto automata.

#automata.printAutomata()

'''Função que faz a equivalencia de estados implementada'''

#estados_equivalentes = AF.equivalents(automata) #Passei para a funçao de minimização

# Se eu passasse "automata" nas duas funções, a função negado iria negar o automato já minimizado,
# pois a função minimum modifica o objeto. Logo, é necessário criar uma cópia para que a função
# negado não negue o automato já minimizado, mas sim o original.
# Também passei a chamada da função SAVE pra dentro de minimum e complement. Para que possam salvar
# os automatos com mnemônicos: min (minimizado) e neg (negado).

'''Função de minimização implementada'''

#minimo = AF.minimum(automata, entrada)

'''Função de complemento immplementada'''

#negado = AF.complement(automata_copy, entrada)

'''Função de retorno dos estados finais implementada'''

#finais = AF.final(negado)

#for f in finais:
#    f.printState()

'''Função de Retornar o estado inicial de um automato implementada'''

#inicial = AF.initial(automata)
#inicial.printState()


'''Função de deletar transições implementada.'''

#transicoes = automata.getTransitions()

#AF.deleteTransition(automata,"0","1","a")

'''Função de adicionar um novo estado'''

#AF.addState(automata,"ADD",False,False)

'''Função de adicionar uma nova transição'''

#AF.addTransition(automata,"1","1","c")
#automata.printTransitions()
#print("*"*15)

'''Função de deletar uma transição'''
#AF.deleteTransition(automata,"1","1","c")
#automata.printTransitions()

'''Função de testar movimentos a partir de uma plavra e um estado'''
#automata.printTransitions()
#resultado = AF.move(automata, 0, "ababa")






