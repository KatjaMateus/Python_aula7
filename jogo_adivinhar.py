
import random
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
computador = random.choice(lista)
while True:
    jogador = int(input("Digite um número entre 1 e 20: "))
    if computador > jogador:
        print("Tá fria! Digite novamente")     
    elif computador < jogador:
        print("Tá quente! Tente novamente: ")
    elif computador == jogador:
        print("Parabéns! Você adivinhou o número!")
        break

