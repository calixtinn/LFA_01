"""
Classe AFDView
@author: Matheus Calixto | Samuel Terra

Classe que implementa a visão do usuário com o sistema.
"""
from tkinter.filedialog import askopenfilename, asksaveasfilename

from Controller.AFDController import AFDController


class AFDView(object):
    """
    Classe que representa a visão todas as funcionalidade um Automoto Finito Deterministico.
    """

    def verificaEntrada(self, fileName):
        """
        Método responsável por verificar o formato do arquivo de entrada.
        :rtype: bool
        """
        resulSplit = fileName.split('.')

        # Verifica se o arquivo esta no formado do JFlap (.jff)
        if len(resulSplit) >= 2 and resulSplit[len(resulSplit) - 1] == 'jff':
            print("Arquivo selecionado: " + fileName)
            return True
        else:
            print('Arquivo de entrada com formato inválido!')
            return False

    def obtemEntradaAfd(self, multiEntrada=False):
        """
        Método reponsavel por ler a entrada do algoritmo.
        Este método recebe como parâmetro uma flag informando se a entrada deve ser chamada mais
        de uma vez, por exemplo, é utilizado se for necessário ler dois arquivo de uma vez só.
        O valor de de multiEntrada será True quando será necessário obter dois AFDs, desta forma,
        sendo o valor True, será questionado ao usuário, duas vezes o aquivo de entrada, sendo
        consequentemente o caminho de entrada do AFD 1 e do AFD 2. Se também a flag multiEntrada
        for True, será retornado um array com os caminhos dos AFDs. Por padrão a flag multiEntrada
        é setada como False, sendo assim, pode ser omitida ao usar a chamado do método e será 
        retornado apenas uma string com o caminho do arquivo. Caso o usuário aperte no botão de
        cancelar, retornará False indicando que foi cancelada a entrada de dados.
        
        :rtype: bool | list | string
        :type multiEntrada: bool
        :return: O caminho do arquivo de o nome estiver no formato correto, False se não estiver ou
                 uma lista de caminho dos arquivos caso seja multiEntrada
        """
        title = 'Abrir automato do JFlap'
        ftypes = [('Arquivo do JFlap', '.jff'), ('All files', '*')]

        # Lê uma entrada simples, com apenas um arquivo jff
        if not multiEntrada:

            # Repete até que o usuário informe um arquivo
            while True:
                # Abre a janela para selecionar um arquivo
                filename = askopenfilename(filetypes=ftypes, title=title)

                # Verifica se foi selecionado algum arquivo
                if filename:
                    if self.verificaEntrada(filename):
                        return filename
                else:
                    # Apertou o botão de cancelar
                    print("Operação cancelada.")
                    return False

        # Lê mais de um arquivo (dois AFDs no contexto do trabalho)
        else:
            arrayCaminhoAfds = []
            i = 0
            # Faz até a quantidade de arquivos, neste caso será necessario 2 arquivos
            while i < 2:
                # Abre a janela para selecionar um arquivo
                filename = askopenfilename(filetypes=ftypes, title=title)

                # Verifica se foi selecionado algum arquivo
                if filename:
                    # Verifica se o arquivo está num formato válido
                    if self.verificaEntrada(filename):
                        # Adiciona o caminho do arquivo na lista de caminhos
                        arrayCaminhoAfds.append(filename)
                        i += 1
                else:
                    # Apertou o botão de cancelar
                    print("Operação cancelada.")
                    return False

            # Retorna a lista de caminhos
            return arrayCaminhoAfds

    def menuModificaAutomato(self):
        """
        Método responsável por printar na tela, o menu interno onde é possível modificar determinado
        automo
        :return: 
        """

        opcao = True
        automato = None

        while opcao:
            if automato is None:
                print("Automato ainda não selecionado.")
            else:
                print("Automato selecionado")

            print("""
                    0.Voltar ao menu anterior
                    1.Carregar automato
                    2.Liberar automato
                    3.Ver estado inicial
                    4.Ver lista de estados finais
                    5.Adicionar estado
                    6.Adicionar transição
                    7.Remove estado
                    8.Remove transição
                    9.Testar palavra
                    10.Testar movimento
                    11.Imprimir AFD no terminal
                    12.Salvar automato em arquivo do JFlap
                    """)
            opcao = int(input("O que você gostaria de fazer?"))

            if opcao is 0:
                opcao = None
            elif opcao is 1:
                automato = self.carregaAutomato()
            elif opcao is 2:
                automato = None
            elif opcao is 3:
                self.getEstadoInicial(automato)
            elif opcao is 4:
                self.getEstadosFinais(automato)
            elif opcao is 5:
                automato = self.adicionaEstado(automato)
            elif opcao is 6:
                automato = self.adicionaTransicao(automato)
            elif opcao is 7:
                automato = self.deletaEstado(automato)
            elif opcao is 8:
                automato = self.deletaTransicao(automato)
            elif opcao is 9:
                self.testaPalavra(automato)
            elif opcao is 10:
                self.testaMovimento(automato)
            elif opcao is 11:
                self.imprimeTerminal(automato)
            elif opcao is 12:
                self.salvaAfd(automato)
            else:
                print("\nNão é uma opção válida, tente novamente.")

    def carregaAutomato(self):
        afdEntrada = self.obtemEntradaAfd()
        if afdEntrada:
            controller = AFDController()
            return controller.load(afdEntrada)
        else:
            return None

    def getEstadoInicial(self, afd):
        if afd:
            controller = AFDController()
            estadoInicial = controller.initial(afd)
            print("Estado inicial do automato: " + estadoInicial.getName())

    def getEstadosFinais(self, afd):
        if afd:
            controller = AFDController()
            estadosFinais = controller.final(afd)

            print("Lista de estados finais:")
            for e in estadosFinais:
                print(e)

    def obtemEntradaTerminal(self, mensagem, simples=False):
        questao = None

        # Tipo 1: Questões de "Sim" ou "Não"
        if not simples:
            sair = False
            while not sair:
                questao = str(input(mensagem + " (s/n)"))
                if questao.lower() == "s":
                    questao = True
                    sair = True
                elif questao.lower() == "n":
                    questao = False
                    sair = True
                else:
                    print("\nNão é uma opção válida, tente novamente.")

        # Tipo 2: Questões simples, apenas obeter um texto de entrada
        else:
            questao = str(input(mensagem))

        return questao

    def adicionaEstado(self, afd):
        if afd:
            print("Adicionar estado ao automato")

            name = self.obtemEntradaTerminal("Informe o nome do novo estado:", True)
            initial = self.obtemEntradaTerminal("Este estado é inicial?")
            final = self.obtemEntradaTerminal("Este estado é final?")

            controller = AFDController()

            af = controller.addState(afd, name, initial, final)

            if af:
                return af

    def deletaEstado(self, afd):
        if afd:
            print("Remover estado do automato")

            id = self.obtemEntradaTerminal("Informe o ID do estado a ser deletado:", True)

            controller = AFDController()
            af = controller.deleteState(afd, id)

            if af:
                return af

    def adicionaTransicao(self, afd):
        if afd:
            print("Adicionar transição ao automato")

            source  = self.obtemEntradaTerminal("Informe o ID do estado de origem:", True)
            target  = self.obtemEntradaTerminal("Informe o ID do estado de destino:", True)
            consume = self.obtemEntradaTerminal("Informe o item do alfabeto de consumo:", True)

            controller = AFDController()

            af = controller.addTransition(afd, source, target, consume)

            if af:
                return af

    def deletaTransicao(self, afd):
        if afd:
            print("Deletar transição ao automato")

            source  = self.obtemEntradaTerminal("Informe o ID do estado de origem:", True)
            target  = self.obtemEntradaTerminal("Informe o ID do estado de destino:", True)
            consume = self.obtemEntradaTerminal("Informe o item do alfabeto de consumo:", True)

            controller = AFDController()

            af = controller.deleteTransition(afd, source, target, consume)

            if af:
                return af

    def testaPalavra(self, afd):
        if afd:
            print("Testar palavra no autmato")

            word = self.obtemEntradaTerminal("Informe a palavra que deseja testar:", True)

            controller = AFDController()
            result = controller.accept(afd, word)

            print(result)

    def testaMovimento(self, afd):
        if afd:
            print("Testar um movimento com uma palavra a partir de um estado")

            word = self.obtemEntradaTerminal("Informe a palavra que deseja testar:", True)
            id = self.obtemEntradaTerminal("Informe o Id do estado a ser testado:", True)

            controller = AFDController()
            controller.move(afd, id, word)

    def imprimeTerminal(self, afd):
        if afd:
            afd.printAutomata()

    def menuPrincipal(self):
        opcao = True

        while opcao:
            print("""
            0.Sair
            1.Ver estados equivalentes
            2.Obter AFD mínimo
            3.Verificar equivalência de dois AFDs
            4.Realizar complemento do AFD
            5.Realizar união de dois AFDs
            6.Realizar intercessão de dois AFDs
            7.Realizar diferença de dois AFDs
            8.Manipular automato
            """)
            opcao = int(input("O que você gostaria de fazer?"))
            if opcao is 0:
                opcao = None
            elif opcao is 1:
                self.equivalenciaEstados()
            elif opcao is 2:
                self.minimoAfd()
            elif opcao is 3:
                self.equivalenciaAfds()
            elif opcao is 4:
                self.complementoAfd()
            elif opcao is 5:
                self.uniaoAfds()
            elif opcao is 6:
                self.intercessaoAfds()
            elif opcao is 7:
                self.diferencaAfds()
            elif opcao is 8:
                self.menuModificaAutomato()
            else:
                print("\nNão é uma opção válida, tente novamente.")

    def salvaAfd(self, afd):

        if afd:
            sair = False

            while not sair:

                opcao = input("Deseja salvar o automato? (s/n) ")

                if opcao.lower() == "s":
                    title = 'Salvar automato como'
                    ftypes = [('Arquivo do JFlap', '.jff'), ('All files', '*')]

                    # Pega o caminho para salvar
                    caminho = asksaveasfilename(filetypes=ftypes, title=title, defaultextension='.jff')
                    if not caminho:
                        print("Operação cancelada.")
                        sair = True

                    controller = AFDController()
                    controller.save(afd, caminho)
                    print("Automato salvo com sucesso!")
                    sair = True
                elif opcao.lower() == "n":
                    print("Você escolheu não salvar")
                    sair = True
                else:
                    print("Opção inválida")

    def equivalenciaEstados(self):
        print("Verificar equivalência de estados")
        print("Informe o automato que deseja verificar a esquivalência de estados...\n")

        afdEntrada = self.obtemEntradaAfd()
        if afdEntrada:
            controller = AFDController()
            afd = controller.load(afdEntrada)
            listaEstadosEquivalentes = controller.equivalent_states(afd)
            print("Lista de estados equivalentes: " + str(listaEstadosEquivalentes))

        return None

    def minimoAfd(self):
        print("Obter o AFD mínimo")
        print("Informe o automato a ser minimizado...\n")

        afdEntrada = self.obtemEntradaAfd()

        if afdEntrada:
            controller = AFDController()
            afd = controller.load(afdEntrada)
            afdMinimo = controller.minimum(afd)

            self.salvaAfd(afdMinimo)

    def equivalenciaAfds(self):
        print("Obter a equivalência de dois automatos")
        print("Informe os automatos que deseja verificar a equivalência...\n")
        afdEntrada = self.obtemEntradaAfd(True)

        if afdEntrada:
            controller = AFDController()
            afd1 = controller.load(afdEntrada[0])
            afd2 = controller.load(afdEntrada[1])

            resultEquivalents = controller.equivalent_automatas(afd1, afd2)

            print(resultEquivalents)
        return None

    def complementoAfd(self):
        print("Obter o complemento de um AFD")
        print("Informe o automato que deseja obter o complemento...\n")

        afdEntrada = self.obtemEntradaAfd()

        if afdEntrada:
            controller = AFDController()
            afd = controller.load(afdEntrada)
            afdComplemento = controller.complement(afd)

            self.salvaAfd(afdComplemento)

    def uniaoAfds(self):
        print("Obter a inião de dois automatos")
        print("Informe os automatos que deseja realizar a união...\n")

        afdEntrada = self.obtemEntradaAfd(True)

        if afdEntrada:
            controller = AFDController()
            afd1 = controller.load(afdEntrada[0])
            afd2 = controller.load(afdEntrada[1])

            resultUniao = controller.union(afd1, afd2)

            self.salvaAfd(resultUniao)

    def intercessaoAfds(self):
        print("Obter a intercessão de dois automatos")
        print("Informe os automatos que deseja realizar a intercessão...\n")

        afdEntrada = self.obtemEntradaAfd(True)

        if afdEntrada:
            controller = AFDController()
            afd1 = controller.load(afdEntrada[0])
            afd2 = controller.load(afdEntrada[1])

            resultIntercessao = controller.intersection(afd1, afd2)

            self.salvaAfd(resultIntercessao)

    def diferencaAfds(self):
        print("Obter a diferença de dois automatos")
        print("Informe os automatos que deseja realizar a diferença...\n")

        afdEntrada = self.obtemEntradaAfd(True)

        if afdEntrada:
            controller = AFDController()
            afd1 = controller.load(afdEntrada[0])
            afd2 = controller.load(afdEntrada[1])

            resultDiferenca = controller.difference(afd1, afd2)

            self.salvaAfd(resultDiferenca)