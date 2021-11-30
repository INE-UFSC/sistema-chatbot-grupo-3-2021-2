#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotMarombeiro import BotMarombeiro
from Bots.BotGamer import BotGamer
from Bots.BotEspelhado import BotEspelhado

###construa a lista de bots disponíveis aqui
lista_bots = [BotMarombeiro("Bambam"), BotGamer("Ninja"), BotEspelhado("oãoJ")]

sys = scb.SistemaChatBot("4FunBots",lista_bots)
sys.inicio()
