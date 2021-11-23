from Bots.Bot import Bot

class BotGamer(Bot):
    def __init__(self,nome):
        self.__nome = nome

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, novo_nome: int):
        self.__nome = novo_nome

    def apresentacao(self):
        print("Bot Gamer: Olá jogadô, Eu sou seu novo parceiro de equipe!")
 
    def mostra_comandos(self):
        print("[0]: Como está o dia hoje?")
        print("[1]: Quem é seu criador?")
        print("[2]: Qual seu jogo favorito?")
        print("[3]: Qual seu rank no seu jogo favorito?")
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        pass

    def despedida(self):
        pass