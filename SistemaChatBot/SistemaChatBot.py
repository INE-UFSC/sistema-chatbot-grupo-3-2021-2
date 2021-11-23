from Bots.Bot import Bot

def verificacao(lista):
    for i in lista:
        if type(i).__name__ == 'Bot':
            x = True

        else:
            x = False
            break

    return x

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        if vericacao(lista_bots):
            self.__lista_bots = lista_bots
            self.__bot = None
        else:
            print('Error! Nem todos os elementos são bots!')
    
    def boas_vindas(self):
        print('Sejam bem vindos a imersão de bots!')

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são:')
        for i in range(len(self.__lista_bots)):
            print(f'{i} - Bot: {i.nome} - Mensagem de apresentação: {i.apresentacao}')

    def escolhe_bot(self):

        entrada = int(input('Digite o número do chat bot desejado:(-1 para encerrar o programa)  '))
        if entrada == -1:
            print('Programa encerrado!')
            return break
        else:
            while entrada <= len(self.__lista_bots) or entrada >= len(self.__lista_bots) :
                print('Valor inválido!')
                entrada = int(input('Digite o número do chat bot desejado: '))

        self.__bot = self.__lista_bots[entrada]

    def mostra_comandos_bot(self):
        bot_c = self.__bot.comandos
        for i in len(bot_c.keys()):
            print(f'{i} - {bot_c.keys()[i]})


    def le_envia_comando(self):
        entrada = int(input('Digite o comando desejado:(-1 para encerrar o programa) '))
        while entrada <= len(self.__bot.comandos) or entrada >= len(self.__bot.comandos):
            print('Valor inválido!')
            entrada = int(input('Digite o comando desejado:(-1 para encerrar o programa) '))


    def inicio(self):
        
