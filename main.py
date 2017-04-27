from Controller.AFDController import AFDController

#Contador de ID's de autômatos. (Auto Increment)
#automata_Id_counter = 0 (Passei pra classe AFDController

AF = AFDController()

automata = AF.load("equivalente_2.jff")
#automata.printAutomata()
estados_equivalentes = AF.equivalents(automata)

print("Lista de estados equivalentes: " + str(estados_equivalentes))

negado = AF.complement(automata)

#minimo = AF.minimum(automata,estados_equivalentes)

AF.save(negado, 'neg_equivalente_2.jff')