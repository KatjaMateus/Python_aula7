def VerAlunos():
    for aluno in cadastro:
        print(cadastro)
    if cadastro == {}:
        print("O cadastro não possui alunos ainda.")
                       
cadastro = {}

def AdicionarAluno():
    matricula = int(input("Número de matrícula: "))
    nome = input("Nome do aluno: ").strip() 
    cadastro.update([[
            matricula , nome]])
    
def RemoverAluno():
    while True:
        VerAlunos()
        if cadastro == {}:
            print("O cadastro não possui alunos ainda.")
            break
        remover = int(input("Digite o número de matrícula do aluno a remover: "))
        del cadastro[remover]
        escolha = int(input("""Continua removendo alunos?
              1 = sim
              2 = não """))
        if escolha == 2:
            break 
    

def AtualizarAluno():
    while True:
        VerAlunos()
        if cadastro == {}:
            print("O cadastro não possui alunos ainda.")
            break
        atualizar = int(input("Digite o número de matrícula do aluno a atualizar: "))
        novo_nome = input("Digite o nome novo do aluno: ")
        cadastro[atualizar]=novo_nome
        escolha = int(input("""Continua atualizando alunos?
              1 = sim
              2 = não """))
        if escolha == 2:
            break

# print("""Escolhe a opção para realizar.""")

# while True:
#     escolha = int(input("""
#     1 - Adicionar aluno
#     2 - Visualizar alunos cadastrados
#     3 - Remover aluno
#     4 - Atualizar aluno
#     0 - Sair
#      """))
#     if escolha == 1:
#         adicionar_alunos()
#     elif escolha == 2:
#         visualizar_alunos()
#     elif escolha == 3:
#         remover_alunos()
#     elif escolha == 4:
#         atualizar_alunos()
#     elif escolha == 0:
#         break
#     else:
#         print("Opção inválida")
