import requests
import unidecode

def criptografa(texto, deslocamento):
    
    codificado = []
    str = ""

    for letra in texto:
	    codifica = ord(letra)

	    if codifica >= 32 and codifica <=64:
		    caracter = chr(codifica)
		    codificado.append(caracter)
		
	    elif codifica == 122:
		    caracter = chr(codifica-25)
		    codificado.append(caracter)

	    else :
		    caracter = chr(codifica+ deslocamento)
		    codificado.append(caracter)

    return(str.join(codificado))

def descriptografa(texto, deslocamento):

	codificado = []
	str = ""

	for letra in texto:
		codifica = ord(letra)

		if codifica >= 32 and codifica <=64:
			caracter = chr(codifica)
			codificado.append(caracter)

		elif codifica == 97:
			caracter = chr(codifica+25)
			codificado.append(caracter)

		else :
			caracter = chr(codifica- deslocamento)
			codificado.append(caracter)

	return(str.join(codificado))


if __name__ == '__main__':

	with open('alienista.txt', "r" ,encoding='utf-8') as arquivo:
		texto = arquivo.read()
		texto = unidecode.unidecode(texto)

	deslocamento = int(input("\nDigite o deslocamento para realizar a encriptacao: "))	

	with open('o-alienista.txt', "w" ,encoding='utf-8') as arquivo:
		arquivo.write(criptografa(texto,deslocamento))

