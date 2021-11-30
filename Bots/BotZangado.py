from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {"Olá, tudo bem ? ": "E o que tem de bom?!",
                           "Como você está ?": "Não interessa!", 
                           "Quero um conselho": "Não tenho filho deste tamanho!", 
                           "Adeus": ""
                           }

    
    def mostra_comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'GRRRRRR Meu nome é {self.nome} e não me incomode!'

    def executa_comando(self, cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("NÃO SEI!")

    def boas_vindas(self):
        return 'Não acredito que você me escolheu!'

    def despedida(self):
        return 'Finalmente, até nunca mais! '
