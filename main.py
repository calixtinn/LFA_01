from Controller.AFDController import AFDController

#Contador de ID's de autômatos. (Auto Increment)
#automata_Id_counter = 0 (Passei pra classe AFDController

AF = AFDController()

automata = AF.load("equivalente_1.jff")
#automata.printAutomata()
estados_equivalentes = AFDController.equivalents(automata)

#print("Lista de estados equivalentes: " + str(estados_equivalentes))

AF.complement(automata)

#AF.minimum(automata,estados_equivalentes)

#AF.save(automata, 'saida1.jff')

for a in automata.getStates():
    print('\n')
    print('Id '+a.getId())
    print('Name '+a.getName())
    print('Posx '+a.getPosx())
    print('Posy '+a.getPosy())
    print('Final? '+str(a.isFinal()))
    print('Inicial? '+str(a.isInitial()))