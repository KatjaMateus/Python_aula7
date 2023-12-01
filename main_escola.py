# FAÇA UM PROGRAMA NA main.py USANDO OS MÓDULOS QUE VOCÊ CRIOU QUE PEDE PARA O USUÁRIO DIGITAR 4 NOTAS E 
# MOSTRA QUAL A MÉDIA DAS NOTAS, 
# QUAL FOI A MAIOR DELAS, QUAL FOI A MENOR DELAS


# FAÇA UM PROGRAMA NA MAIN QUE PEDE PARA O USUÁRIO DIGITAR UMA PALAVRA E MOSTRE NA TELA 
# SE ELA É UM PALINDROMO, QUANTOS CARACTERES AQUELA PALAVRA TEM, E QUANTAS DELAS SÃO VOGAIS E 
# QUANTAS CONSOANTES

from escola.matemática import *
from escola.portugues import *

lista_de_notas = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    lista_de_notas.append(nota)

print(media_numeros(lista_de_notas))
print(maior_numero(lista_de_notas))
print(menor_numero(lista_de_notas))

palavra = str(input("Digite uma palvra: "))
invertida = inverter_texto(palavra)
if palavra == invertida:
    print("É um palídromo")
else:
    print("Não é um palíndromo")

print(f"A palavra digitada possui {contar_caracteres(palavra)}")
print(f"Número de vogais é: {contar_vogais_e_consoantes(palavra)[0]}")
print(f"Número de consoantes é: {contar_vogais_e_consoantes(palavra)[1]}")
