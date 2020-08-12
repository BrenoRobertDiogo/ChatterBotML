#-*- coding: utf-8 -*-
import re
import time
from os import system
from datetime import datetime
import random
import pesquisa
from responder import responder
from pesquisa import defina, definicao

def main():
	frase = ''
	nome = str(input('Bot: Diga-me seu nome: '))
	botNome = str(input('Bot: Agora o meu nome por gentileza: '))
	while frase!='sair':
		frase = str(input(f'{nome}: '))
		resposta = responder(frase)
		print(f'{botNome}: {resposta}')

main()