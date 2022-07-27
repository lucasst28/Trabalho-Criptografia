import unidecode
import operator

def decodifica(texto, frequencia):

    letracomumAlfabeto = max(frequencia.items(), key=operator.itemgetter(1))[0]
    letradotexto = freq(texto)
    letracomumTexto = max(letradotexto.items(), key = operator.itemgetter(1))[0]
    deslocamento = abs(ord(letracomumTexto)) - ord(letracomumAlfabeto)
    return descriptografa(texto, deslocamento)



    


def freq(texto):

    dicio = dict()
    tam = 0
    for x in texto:
        if x not in dicio:
            dicio[x] = 1
        else:
            dicio[x] += 1
    
    
    for key in dicio:
        tam += dicio[key]
    
    tam -= (dicio[','] + dicio['.'] + dicio['-'] + dicio[' '])

    for key in dicio:
        dicio[key] = dicio[key]/tam*100
    
    dicio.pop(' ', -1)
        
    return dicio

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

    with open('alienista.txt', encoding='utf-8') as f:
        livro = f.read()
    frequencia = freq(unidecode.unidecode(livro.lower()))

    with open('o-alienista.txt', encoding='utf-8') as f:
        texto = f.read()

    resultado = decodifica(texto, frequencia)
    
    with open('o-alienistia-descript.txt',"w" ,encoding='utf-8') as arquivo:
        arquivo.write(resultado)

    