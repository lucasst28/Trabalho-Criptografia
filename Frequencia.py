import unidecode
def frequencia(texto):
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

    dicio.pop(' ', -1)
    return str(dicio)
    
    


if __name__ == '__main__':

	with open('o-alienista.txt', "r" ,encoding='utf-8') as arquivo:
		texto = arquivo.read()
		texto = unidecode.unidecode(texto.lower())


	with open('frequencia2.txt', "w" ,encoding='utf-8') as arquivo:
		arquivo.write(frequencia(texto))
