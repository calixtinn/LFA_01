from Controller.AFDController import AFDController

#Contador de ID's de autômatos. (Auto Increment)
#automata_Id_counter = 0 (Passei pra classe AFDController

AF = AFDController()

automata = AF.load("equivalente_1.jff")
#automata.printAutomata()
estados_equivalentes = AFDController.equivalents(automata)

#print("Lista de estados equivalentes: " + str(estados_equivalentes))

AF.complement()

#AF.minimum(automata,estados_equivalentes)

AF.save(automata, 'saida1.xml')