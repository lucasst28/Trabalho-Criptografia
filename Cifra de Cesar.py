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

	##texto = unidecode.unidecode(input("Escreva a mensagem para criptografa-la: "))

	##deslocamento = int(input("\nDigite o deslocamento para realizar a encriptacao: "))	

	arquivo = open('o-alienista', 'r')
	conteudo = arquivo.readlines
	print(conteudo)
	##texto = criptografa(texto, deslocamento)
	##print("\n")
	##print(texto)
	##print("\n")
	##print(descriptografa(texto, deslocamento))
