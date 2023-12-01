# CRIE UM PACOTE CHAMADO escola QUE CONTENHA UM MÓDULO CHAMADO matemática QUE TENHA DENTRO DELE AS FUNÇÕES:
# maior_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MAIOR DELES)
# menor_numero (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA O MENOR DELES)
# media_numeros (QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA A MÉDIA DELES)
# DENTRO DO MESMO PACOTE escola, CRIE UM MÓDULO CHAMADO português QUE TENHA DENTRO DELE AS FUNÇÕES:
# inverter_texto (QUE RECEBE UM TEXTO E RETORNA ELE INVERTIDO)
# contar_caracteres (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE CARACTERES DAQUELE TEXTO)
# contar_vogais_e_consoantes (QUE RECEBE UM TEXTO E RETORNA A QUANTIDADE DE VOGAIS E A QUANTIDADE DE CONSOANTES QUE AQUELE TEXTO TEM)
# obs: pode retornar uma lista ou um dicionário com os dois valores

def inverter_texto(texto):
    return texto[::-1]

def contar_caracteres(texto):
    contador = 0
    for letra in texto:
        contador += 1
    return contador

def contar_vogais_e_consoantes(texto):
    contador_vogais = 0
    contador_consoantes = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador_vogais += 1
        elif letra.lower() in "bcdfghjklmnpqrstvxyzw":
            contador_consoantes += 1
    return [contador_consoantes, contador_vogais]
        