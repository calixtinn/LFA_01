from Controller.AFDController import AFDController

#Contador de ID's de autômatos. (Auto Increment)
#automata_Id_counter = 0 (Passei pra classe AFDController

AF = AFDController()

automata = AF.load("equivalente_2.jff")
#automata.printAutomata()
estados_equivalentes = AFDController.equivalents(automata)

#print("Lista de estados equivalentes: " + str(estados_equivalentes))

#AF.complement()

minimo = AF.minimum(automata,estados_equivalentes)

AF.save(minimo, 'equivalente_2.jff')