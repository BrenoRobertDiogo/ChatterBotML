from pesquisa import defina, definicao
import re
from datetime import datetime
def responder(frase):
	perguntasUser = {
		r'[Cc]omo esta voc.+?':['Estou muito bem','Fazendo muitos calculos'],
   		r'[Ss]eu dia est. feli+z?':['Sim eu estou muito feliz', 'Com você esse dia melhora', 'Sim meu caro'],
        r'[Qq]ue horas s.o?':f'{datetime.utcnow()}'
    }
	definir = {
    	r'.* [Dd]efina (.*)': defina(frase),
    	r'[Oo] que [éÉeE] (.*)': defina(frase)
    }

	if frase[-1]=='?':
		for per in perguntasUser:
			if re.search(frase, per).group(0) in perguntasUser:
				return perguntasUser[random.choice(per)]
	
	elif re.search(frase, valor).group(0) in [valor for valor in definir]:
		return valor