#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotMarombeiro import BotMarombeiro
from Bots.BotFeliz import BotFeliz
from Bots.BotGamer import BotGamer

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Grumpy"), BotMarombeiro("Bambam"), BotFeliz("Smurf"), BotGamer("Ninja")]

sys = scb.SistemaChatBot("4FunBots",lista_bots)
sys.inicio()
