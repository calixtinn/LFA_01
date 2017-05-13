from tkinter.filedialog import askopenfilename


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

        # Lê uma entrada simples, com apenas um arquivo jff
        if not multiEntrada:

            # Repete até que o usuário informe um arquivo
            while True:
                # Abre a janela para selecionar um arquivo
                filename = askopenfilename(filetypes=(("Arquivo JFlap", "*.jff"), ("All files", "*.*")))

                # Verifica se foi selecionado algum arquivo
                if filename:
                    if self.verificaEntrada(filename):
                        return filename
                else:
                    # Apertou o botão de cancelar
                    return False

        # Lê mais de um arquivo (dois AFDs)
        else:
            arrayCaminhoAfds = []
            i = 0
            # Faz até a quantidade de arquivos, neste caso será necessario 2 arquivos
            while i < 2:
                # Abre a janela para selecionar um arquivo
                filename = askopenfilename(filetypes=(("Arquivo JFlap", "*.jff"), ("All files", "*.*")))

                # Verifica se foi selecionado algum arquivo
                if filename:
                    # Verifica se o arquivo está num formato válido
                    if self.verificaEntrada(filename):
                        # Adiciona o caminho do arquivo na lista de caminhos
                        arrayCaminhoAfds.append(filename)
                        i += 1
                else:
                    # Apertou o botão de cancelar
                    return False

            # Retorna a lista de caminhos
            return arrayCaminhoAfds

    def menu(self):
        opcao = True
        while opcao:
            print("""
            0.Sair
            1.Abir arquivo do JFlap
            2.Salvar AFD como arquivo do JFlap
            3.Ver estados equivalentes
            4.Obter AFD mínimo
            5.Verificar equivalência de dois AFDs
            6.Realizar complemento do AFD
            7.Realizar união de dois AFDs
            8.Realizar intercessão de dois AFDs
            9.Realizar diferença de dois AFDs
            10.Testar palavra no AFD
            11.Testar movimento do AFD
            12.Adicionar estado ao AFD
            13.Deletar estado do AFD
            14.Adicionar transição ao AFD
            15.Deletar transição do AFD
            16.Imprimir AFD no terminal
            """)
            opcao = int(input("O que você gostaria de fazer? "))
            if opcao is 0:
                opcao = None
            elif opcao is 1:
                self.abrirArquivo()
            elif opcao is 2:
                self.salvaAfd()
            elif opcao is 3:
                self.equivalenciaEstados()
            elif opcao is 4:
                self.menimoAfd()
            elif opcao is 5:
                self.equivalenciaAfds()
            elif opcao is 6:
                self.complementoAfd()
            elif opcao is 7:
                self.uniaoAfds()
            elif opcao is 8:
                self.intercessaoAfds()
            elif opcao is 9:
                self.diferencaAfds()
            elif opcao is 10:
                self.testaPalavra()
            elif opcao is 11:
                self.testaMovimento()
            elif opcao is 12:
                self.adicionaEstado()
            elif opcao is 13:
                self.deletaEstado()
            elif opcao is 14:
                self.adicionaTransicao()
            elif opcao is 15:
                self.deletaTransicao()
            elif opcao is 16:
                self.imprimeTerminal()
            else:
                print("\n Não é uma opção válida, tente novamente.")

    def abrirArquivo(self):
        pass

    def salvaAfd(self):
        pass

    def equivalenciaEstados(self):
        pass

    def menimoAfd(self):
        pass

    def equivalenciaAfds(self):
        pass

    def complementoAfd(self):
        pass

    def uniaoAfds(self):
        pass

    def intercessaoAfds(self):
        pass

    def diferencaAfds(self):
        pass

    def testaPalavra(self):
        pass

    def testaMovimento(self):
        pass

    def adicionaEstado(self):
        pass

    def deletaEstado(self):
        pass

    def adicionaTransicao(self):
        pass

    def deletaTransicao(self):
        pass

    def imprimeTerminal(self):
        pass
