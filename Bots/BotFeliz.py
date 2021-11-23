from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print("Bot Feliz: 'Olá eu sou o Fulico, estou muito feliz que você me escolheu, YAAAY!!'")
 
    def mostra_comandos(self):
        
        pass
    
    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        print("Bot Feliz: ''")
        pass
    
    def conte_piada(self):
        print("Bot Feliz: 'Qual é a cidade que quando chove molha os bêbados? Bar-sem-lona' *BA-DUM-TSS*")

    def despedida(self):
        print("Bot Feliz: ''")
        pass