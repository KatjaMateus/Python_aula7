from prova7_funcoes import*

print("""Escolhe a opção para realizar.""")

while True:
    escolha = int(input("""
    1 - Adicionar aluno
    2 - Visualizar alunos cadastrados
    3 - Remover aluno
    4 - Atualizar aluno
    0 - Sair
     """))
    
    if escolha == 1:
        AdicionarAluno()
    elif escolha == 2:
        VerAlunos()
    elif escolha == 3:
        RemoverAluno()
    elif escolha == 4:
        AtualizarAluno()
    elif escolha == 0:
        break
    else:
        print("Opção inválida")