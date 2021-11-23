# from Bots.Bot import Bot
from datetime import datetime

class BotGamer():
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {
            "Como está seu dia hoje?": "Contando que agora são " + datetime.now().strftime('%H:%M') + "já ganhei mais de 10 ranqueadas no Rainbow Six",
            "Quem é seu criador?": "Meu criador é o Grupo 3, do Curso de POO 2!", 
            "Qual seu jogo favorito?": "Meu jogo favorito é o Counter Strike: GO", 
            "Qual seu rank no seu jogo favorito?": "Sendo bem modesto, sou Global 😎", 
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
        print(f"{self.__nome}: Eu sou o {self.__nome}! O bot mais insano desse sistema.")
 
    def mostra_comandos(self):
        return self.comandos

    def executa_comando(self,cmd):
        pass

    def boas_vindas(self):
        print(f"{self.__nome}: Olá jogadô, eu sou seu novo parceiro de equipe!")

    def despedida(self):
        print(f"{self.__nome}: Até a próxima partida meu parceiro!")