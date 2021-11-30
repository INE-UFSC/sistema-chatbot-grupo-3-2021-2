from Bots.Bot import Bot

class BotEspelhado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = {"Conte uma curiosidade":"...moc.scilobmys es-avamahC .5891 ed oçram ed 51 me odartsiger iof tenretnI ed oinímod oriemirp O"
                           "Conte uma piada":"...méugnin me anrep a assap oãn ale euqrop ,arboc A ?odnum od otsenoh siam lamina o lauQ"
                           "Como ser um Bot Espelhado":"...lamron uos ue ,êcov é odahlepse é meuq mim arP"}
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print("Bot Espelhado: '...oditrevni é olaf euq odut ,odahlepsE toB o ", self.__nome," uos ue ,álO'")
 
    def mostra_comandos(self):
        return self.__comandos
    
    def executa_comando(self,cmd):
         try:
            return self.__comandos[cmd]
        except:
            print("...rezaf ogisnoc oãn ue ossI")

    def boas_vindas(self):
        print("Bot Espelhado: '...rednetne em agisnoc euq orepse ,uehlocse em êcoV'")

    def despedida(self):
        print("Bot Espelhado: '...amixórp a éta ,êcov moc rasrevnoc rezarp mu ioF'")