import unidecode

def decodifica(texto, freq):

    codificado = []
    str = ''
    

    


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
        dicio[key] = dicio[key]/tam
    
    dicio = sorted(dicio.items(), key = lambda t: t[0])
        

    return dicio

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

if __name__ == '__main__':

    texto = unidecode.unidecode(input("Digite o texto: "))
    freq = freq(texto)
    print(freq)
    
    #criptografa = criptografa(texto)

    #print(decodifica(criptografa, freq))
