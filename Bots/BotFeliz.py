from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            "Qual o seu nome?": f"{self.nome} :D", 
            "Quero um conselho": "Sorria, a vida é uma só!", 
        }

    #nao esquecer o decorator
    @property
    def nome(self):
        return self.__nome

    #nao esquecer o decorator
    @nome.setter
    def nome(self, novo_nome: int):
        self.__nome = novo_nome
    
    @property
    def comandos(self):
        return self.__comandos

    @comandos.setter
    def comandos(self, novo_comandos: int):
        self.__comandos = novo_comandos
        
    def apresentacao(self):
        return(f"Meu nome é {self.nome}! Fico muito feliz de conversar com você :) !!!")
 
    def mostra_comandos(self):
        return self.comandos

    def executa_comando(self,cmd):
        try:
            return self.comandos[cmd]
        except:
            return ("Comando inválido")

    def boas_vindas(self):
        return(f"{self.nome}: Olá, como você está? Obrigado por me chamar!")

    def despedida(self):
        return(f"{self.nome}: Tenha um bom dia!")