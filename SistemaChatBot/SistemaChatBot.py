from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        for i in lista_bots:
            if isinstance(i,Bot):
                ehBot = True
            else:
                ehBot = False
                break

        self.__empresa = nomeEmpresa
        if ehBot:
            self.__lista_bots = lista_bots
            self.__bot = None
        else:
            raise print('Erro! Nem todos os elementos são bots!')
    
    def boas_vindas(self):
        print(f'Sejam bem vindos à imersão de bots da {self.__empresa}!')

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são:')
        for i in range(len(self.__lista_bots)):
            print(f'{i+1} - Bot: {self.__lista_bots[i].nome} - Mensagem de apresentação: {self.__lista_bots[i].apresentacao()}')

    def escolhe_bot(self):

        entrada = int(input('Digite o número do chat bot desejado:(-1 para encerrar o programa)  '))
        if entrada == -1:
            print('Programa encerrado!')
            return True
        else:
            while entrada < 0 or entrada > len(self.__lista_bots) :
                print('Valor inválido!')
                entrada = int(input('Digite o número do chat bot desejado: '))

            self.__bot = self.__lista_bots[entrada-1]
            return False

    def mostra_comandos_bot(self):
        bot_c = self.__bot.mostra_comandos()
        index = 0
        for i in bot_c:
            print(f'{index} - {i}')
            index += 1

    def le_envia_comando(self):
        entrada = int(input('Digite o comando desejado:(-1 para encerrar o programa) '))
        if entrada == -1:
            return True

        while entrada < -1 or entrada >= len(self.__bot.mostra_comandos()):
            print('Valor inválido!')
            entrada = int(input('Digite o comando desejado:(-1 para encerrar o programa) '))

        list_temp = []
        dic = self.__bot.mostra_comandos()
        for el in dic:
            list_temp.append(dic[el])

        print(f'{self.__bot.nome} diz: {list_temp[entrada]}')
        return False

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot
        check = self.escolhe_bot()
        if check:
            return print("Tchau!")
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        while True:
            self.mostra_comandos_bot()
            end = self.le_envia_comando()
            if end:
                print(self.__bot.despedida())
                break
