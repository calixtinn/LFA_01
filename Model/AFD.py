"""
@AFD
@author: Matheus Calixto | Samuel Terra
Esta classe representa um Automoto Finito Deterministico.
"""

# --------------------------------------  O que um AFD tem? (Esta classe) ------------------------------------------
#
# Estados, transições, Id
#
# Lista de todos estados
# Estado inicial
# Lista de estados finais
# Lista de transições
# ?Alfabeto?Tabela ASCII?
#
# -----------------------------------------  Comentarios dos metodos -----------------------------------------------
#
# AFD m;
# m.load("entrada.jff") ;
#
# AFD m;
# m.salve("saida.jff") ;
#
# O usuário deseja poder identificar estados equivalentes, além de obter uma versão mínima do AFD.
# AFD m, mm;
# List eqv;
#
# eqv = m.equivalents() ;
# mm = m.minimum() ;
#
# O usuário deseja poder comparar dois AFDs para saber se são ou não equivalentes.
#
# AFD m1, m2;
#
# if (AFD.equivalents(m1, m2))
#   print("sim");
#       else
#   print("não") ;
#
# O usuário deseja poder realizar operações de complementação, união, intersessão e diferença.
#
# AFD m1, m2, m3, m4, m5, m6;
#
# m3 = m1.complement();
# m4 = m1.union(m2) ;
# m5 = m1.intersection(m2);
# m6 = m1.difference(m2) ;
#
# O usuário deseja poder consultar o AFD, testar a pertença de uma palavra na linguagem, testar movimentos.
#
# AFD m;
# int estado ;
#
# m.accept("aaabbbaa")
# estado = m.initial();
# estado = m.move(estado,"aaab");
# estado in m.finals()
#
#
# O usuário deseja poder alterar o AFD.
# AFD m;
#
# m.addState(id=10, initial=false, final=true);
# m.addTransition(source=1, target=2, consume="b");
# m.deleteState(3);
# m.deleteTransition(source=1 ,target=4, consume="a");
#
# ------------------------------------------  Implementações do AFD ------------------------------------------------
# AFD m
# m.load("entrada.jff");
# m.salve("saida.jff");
# List eqv = m.equivalents();
# AFD mm = m.minimum();
# True|False = AFD.equivalents(m1, m2)
# AFD m3 = m1.complement();
# AFD m4 = m1.union(m2);
# AFD m5 = m1.intersection(m2);
# AFD m6 = m1.difference(m2);
# True|False m.accept("aaabbbaa")
# State estado = m.initial();
# State estado = m.move(estado ,"aaab") ;
# List m.finals()
# m.addState(id=10, initial=false, final=true);
# m.addTransition(source=1, target=2, consume="b");
# m.deleteState(3);
# m.deleteTransition(source=1 ,target=4, consume="a");
# ----------------------------------------------------------------------------------------------------------------

from Model.State import State
from Model.Transition import Transition

class AFD(object):

    def __init__(self, Id, States, Transitions, Initial, Finals, Alphabet):
        self.Id = Id
        self.States = States
        self.Transitions = Transitions
        self.Initial = Initial
        self.Finals = Finals
        self.Alphabet = Alphabet

    def printAutomata(self):
        """
        Metodo responsavel por printar os estados do autômato e suas características.
        """
        for i in self.States: # Para cada objeto State
            trans = ""
            for j in self.Transitions: # Para cada objeto Transition
                if (j.getFrom() == i.getId()): # Se From = ID do estado, a transição faz parte do estado.
                    trans += Transition.printTransition(j) # Cria uma String com as transições de cada estado.
            State.printState(i, trans)
        print("Alfabeto: " + str(self.Alphabet))

    def getStates(self):
        return self.States

    def getAlphabet(self):
        return self.Alphabet

    def getTransitions(self):
        return self.Transitions

    def setStates(self, States):
        self.States = States

    def setTransitions(self, Transitions):
        self.Transitions = Transitions