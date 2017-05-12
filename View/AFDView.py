from tkinter.filedialog import askopenfilename
from pip._vendor.distlib.compat import raw_input

class AFDView(object):
    """
    Classe que implementa todas as funcionalidade um Automoto Finito Deterministico.
    """

    def entrada(self):
        filename = askopenfilename()
        resulSplit = filename.split('jff')

        if len(resulSplit) is 1:
            print('Arquivo de entrada no formato inválido!')
        else:
            print('Certo')

    def abrirArquivo(self):
        pass

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
            opcao = int(raw_input("O que você gostaria de fazer? "))
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
