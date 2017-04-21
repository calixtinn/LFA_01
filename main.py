
from Controller.AFDController import AFDController

#Contador de ID's de autômatos. (Auto Increment)
automata_Id_counter = 0

AFD = AFDController()

automata = AFD.load("a_b_impar.jff", automata_Id_counter)
automata_Id_counter += 1
automata.printAutomata()