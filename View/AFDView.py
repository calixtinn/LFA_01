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

    def entrada(self, multiEntrada=False):
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

        automato = None

        opcao = True
        while opcao:
            if automato is None:
                print("Automato ainda não selecionado.")
            else:
                print("Automato selecionado")
            print("""
                    0.Voltar ao menu anterior
                    1.Carregar automato
                    2.Liberar automato
                    3.Adicionar estado
                    4.Adicionar transição
                    5.Remove estado
                    6.Remove transição
                    """)
            opcao = int(input("O que você gostaria de fazer? "))

            if opcao is 0:
                opcao = None
            elif opcao is 1:
                automato = self.entrada()
            elif opcao is 2:
                automato = None
            elif opcao is 3:
                self.adicionaEstado()
            elif opcao is 4:
                self.deletaEstado()
            elif opcao is 5:
                self.adicionaTransicao()
            elif opcao is 6:
                self.deletaTransicao()
            else:
                print("\nNão é uma opção válida, tente novamente.")

    def adicionaEstado(self):
        pass

    def deletaEstado(self):
        pass

    def adicionaTransicao(self):
        pass

    def deletaTransicao(self):
        pass

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
            8.Testar palavra no AFD
            9.Testar movimento do AFD
            10.Modificar automato
            11.Imprimir AFD no terminal
            """)
            opcao = int(input("O que você gostaria de fazer? "))
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
                self.testaPalavra()
            elif opcao is 9:
                self.testaMovimento()
            elif opcao is 10:
                self.menuModificaAutomato()
            elif opcao is 11:
                self.imprimeTerminal()
            else:
                print("\n Não é uma opção válida, tente novamente.")

    def salvaAfd(self, afd):

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

        afdEntrada = self.entrada()
        controller = AFDController()
        afd = controller.load(afdEntrada)
        listaEstadosEquivalentes = controller.equivalent_states(afd)
        print("Lista de estados equivalentes: " + str(listaEstadosEquivalentes))

    def minimoAfd(self):
        print("Obter o AFD mínimo")
        print("Informe o automato a ser minimizado...\n")
        afdEntrada = self.entrada()
        controller = AFDController()
        afd = controller.load(afdEntrada)
        afdMinimo = controller.minimum(afd)

        self.salvaAfd(afdMinimo)

    def equivalenciaAfds(self):
        print("Obter a equivalência de dois automatos")
        print("Informe os automatos que deseja verificar a equivalência...\n")
        afdEntrada = self.entrada(True)

        controller = AFDController()
        afd1 = controller.load(afdEntrada[0])
        afd2 = controller.load(afdEntrada[1])

        resultEquivalents = controller.equivalent_automatas(afd1, afd2)

        print(resultEquivalents)

    def complementoAfd(self):
        print("Obter o complemento de um AFD")
        print("Informe o automato que deseja obter o complemento...\n")
        afdEntrada = self.entrada()
        controller = AFDController()
        afd = controller.load(afdEntrada)
        afdComplemento = controller.complement(afd)

        self.salvaAfd(afdComplemento)

    def uniaoAfds(self):
        print("Obter a inião de dois automatos")
        print("Informe os automatos que deseja realizar a união...\n")
        afdEntrada = self.entrada(True)

        controller = AFDController()
        afd1 = controller.load(afdEntrada[0])
        afd2 = controller.load(afdEntrada[1])

        resultUniao = controller.union(afd1, afd2)

        self.salvaAfd(resultUniao)

    def intercessaoAfds(self):
        print("Obter a intercessão de dois automatos")
        print("Informe os automatos que deseja realizar a intercessão...\n")
        afdEntrada = self.entrada(True)

        controller = AFDController()
        afd1 = controller.load(afdEntrada[0])
        afd2 = controller.load(afdEntrada[1])

        resultIntercessao = controller.intersection(afd1, afd2)

        self.salvaAfd(resultIntercessao)

    def diferencaAfds(self):
        print("Obter a diferença de dois automatos")
        print("Informe os automatos que deseja realizar a diferença...\n")
        afdEntrada = self.entrada(True)

        controller = AFDController()
        afd1 = controller.load(afdEntrada[0])
        afd2 = controller.load(afdEntrada[1])

        resultDiferenca = controller.difference(afd1, afd2)

        self.salvaAfd(resultDiferenca)

    def testaPalavra(self):
        pass

    def testaMovimento(self):
        pass

    def imprimeTerminal(self):
        pass
