from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {"1": "Olá, tudo bem ? ",
                           "2": "Como você está ?", "3": "Quero um conselho", "4": "Adeus"}

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return f'GRRRRRR Meu nome é {self.nome} e não me incomode!'

    def executa_comando(self, cmd):
        if cmd == '1':
            return f' {self.nome} diz: E o que tem de bom?!'
        elif cmd == '2':
            return f' {self.nome} diz: Não interessa!'
        elif cmd == '3':
            return f' {self.nome} diz:Não tenho filho deste tamanho!'
        elif cmd == '4':
            return self.despedida()
        else:
            return f'Comando não encontrado'

    def boas_vindas(self):
        return f' {self.nome} diz: Não acredito que você me escolheu!'

    def despedida(self):
        return f' {self.nome} diz: Finalmente, até nunca mais! '
