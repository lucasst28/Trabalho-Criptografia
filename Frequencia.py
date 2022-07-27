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

    return dicio
    
    


if __name__ == '__main__':

    texto = unidecode.unidecode(input("Digite o texto: "))
    texto = texto.lower()
    dicionario = frequencia(texto)
    print(dicionario)
