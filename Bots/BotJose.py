from Bots.Bot import Bot

class BotJose(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            "conselho para os estudos": "José analisa suas nota\nJosé diz: Desistir é para os fracos, o ideal é nem tentar",
            "conselho amoroso": "José analisa seu Tinder\nJosé diz: Nunca é tarde para um novo fracasso",
            "conselho para a carreira": "José te entrega um guia de como se comportar numa entrevista\nRegra 1: chame o empregador de 'meu parça', é contrato na certa",
            "adeus": "José diz: Vamos esquecer os erros do passado, meu amigo, e focar nos erros do futuro. Adeus, até vista"}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        msg = f'Mensagem de apresentação: Olá, eu sou o {self.__nome}, seu bot conselheiro'
        return msg
    def mostra_comandos(self):
        return self.__comandos
    
    def executa_comando(self,cmd):
        try:
            return self.__comandos[cmd]
        except:
            print("Você está louco?")

    def boas_vindas(self):
        return "José diz: Que bom que você me escolheu! Espero que eu possa te ajudar"
    

    def despedida(self):
        return "José diz: Vamos esquecer os erros do passado, meu amigo, e focar nos erros do futuro. Adeus, até vista"