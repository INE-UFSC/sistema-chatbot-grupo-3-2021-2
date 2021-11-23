from Bots.Bot import Bot

class BotMarombeiro(Bot):
    def __init__(self, nome: str):
        self.__nome = nome
        self.__comandos = {
            "Me passa um treino?": "3x10 supino\n3x10 barra fixa\n3x10 rosca direta\n3x10 tríceps testa\n(perna não precisa)",
            "Conselho": "Quer ficar grande? Tem que comer e treinar todo dia!", 
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "Treino e dieta eu não furo, tá ligado?"
 
    def mostra_comandos(self):
        return self.__comandos
    
    def executa_comando(self,cmd):
        return self.__comandos[cmd]

    def boas_vindas(self):
        return "HORA DO SHOW P****!"

    def despedida(self):
        return "Valeu mermão, até a próxima."