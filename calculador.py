
from operacoes import *

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while True:
    menu = int(input("""
    Selecione uma operação:
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    match menu:
        case 1:
            print(somar(numero1, numero2))
        case 2:
            print(subtrair(numero1, numero2))
        case 3:
            print(multiplicar(numero1, numero2))
        case 4:
            print(dividir(numero1, numero2))
        case 0:
            print("Fim do programa")
            break
        case _:
            print("Opção Inválida")



    # if menu == 1:
    #     print(somar(numero1, numero2))
    # elif menu == 2:
    #     print(subtrair(numero1, numero2))
    # elif menu == 3:
    #     print(multiplicar(numero1, numero2))
    # elif menu == 4:
    #     print(dividir(numero1, numero2))
    # elif menu == 0:
    #     print("Fim do programa")
    #     break
    # else:
    #     print("Opção Inválida")
