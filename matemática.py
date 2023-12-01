# CRIE UM PACOTE CHAMADO escola QUE CONTENHA UM MÓDULO CHAMADO matemática QUE TENHA DENTRO DELE AS FUNÇÕES:
# maior_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MAIOR DELES)
# menor_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MENOR DELES)
# media_numeros (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA A MÉDIA DELES)
# DENTRO DO MESMO PACOTE escola, CRIE UM MÓDULO CHAMADO português QUE TENHA DENTRO DELE AS FUNÇÕES:
# inverter_texto (QUE RECEBE UM TEXTO E RETORNA ELE INVERTIDO)
# contar_caracteres (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE CARACTERES DAQUELE TEXTO)
# contar_vogais_e_consoantes (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE VOGAIS E A QUANTIDADE DE CONSOANTES QUE AQUELE TEXTO TEM)
# obs: pode retornar uma lista ou um dicionário com os dois valores

def maior_numero (lista):
    pp = lista[0]
    for num in lista:
        if num > pp:
            num = pp
    return pp

def menor_numero (lista):       #na print pede lista
    pp = lista[0]
#def menor_numero(*numeros):  > na print pede numeros, não lista
#   menor = numeros[0]
    for num in lista:
        if num < pp:
            num = pp
    return pp

def media_numeros (lista):
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)