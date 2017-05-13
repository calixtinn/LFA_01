from tkinter.filedialog import askopenfilename


class AFDView(object):
    """
    Classe que representa a visão todas as funcionalidade um Automoto Finito Deterministico.
    """

    def entrada(self, multiEntrada=False):
        """
        Método reponsavel por ler a entrada do algoritmo.
        Este método recebe como parâmetro uma flag informando se a entrada deve ser chamada mais
        de uma vez, por exemplo, é utilizado se for necessário ler dois arquivo de uma vez só.
        O valor de de multiEntrada será True quando será necessário obter dois AFDs, desta forma,
        sendo o valor True, será questionado ao usuário, duas vezes o aquivo de entrada, sendo
        consequentemente o caminho de entrada do AFD 1 e do AFD 2. Se também a flag multiEntrada
        for True, será retornado um array com os caminhos dos AFDs. Por padrão a flag multiEntrada
        é setada como False, sendo assim, pode ser omitida ao usar a chamado do método.
        
        :type multiEntrada: bool
        :rtype: object
        :return: O caminho do arquivo de o nome estiver no formato correto ou None se não estiver
        """

        if not multiEntrada:
            filename = askopenfilename()

            if filename:
                resulSplit = filename.split('.')

                # Verifica se o arquivo esta no formado do JFlap (.jff)
                if len(resulSplit) >= 2 and resulSplit[len(resulSplit) - 1] == 'jff':
                    return filename
                else:
                    print('Arquivo de entrada com formato inválido!')
                    return None
            else:
                print("Botao cancelar")

        else:
            arrayCaminhoAfds = []
            i = 0
            while i < 2:
                filename = askopenfilename()

                # Se retornou algo do widget, realiza o split
                if filename:
                    resulSplit = filename.split('.')

                    # Verifica se o arquivo esta no formado do JFlap (.jff)
                    if len(resulSplit) >= 2 and resulSplit[len(resulSplit) - 1] == 'jff':
                        arrayCaminhoAfds.append(filename)
                        print("Arquivo selecionado: " + filename)
                        i += 1
                    else:
                        print("O arquivo não apresenta um formato inválido!")
                else:
                    print("Botao cancelar")

            print(arrayCaminhoAfds)
            print(len(arrayCaminhoAfds))
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
