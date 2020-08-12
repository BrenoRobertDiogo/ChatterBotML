from requests import get
from bs4 import BeautifulSoup
import urllib.request
import re



def defina(palavra):
	palavra = palavra.lower()
	url = f'https://www.dicionarioinformal.com.br/{palavra}/'
	url = get(url)
	try:
		soup = BeautifulSoup(url, 'html.parser')#Pegando url
		definicao = soup.find('p', class_='text-justify')#Só quero um mesmo
		if definicao!=None: return definicao
		return 'Desculpe-me, não achei nada sobre, talvez você digitou errado'
	except:
		return None

def definicao(frase):
	frase = re.sub(' ', '_', frase)
	url = f'https://pt.wikipedia.org/wiki/{frase}'
	try:
		url = urllib.request.urlopen(url)
		soup = BeautifulSoup(url, 'lxml')
		valor1 = soup.find(id='mw-content-text')
		valorFinal = valor1.find('p')
		valorFinal = valorFinal.text
		if valorFinal !=None: return valorFinal
		return 'Desculpe-me, não achei nada sobre, talvez você digitou errado'
	except:
		return None