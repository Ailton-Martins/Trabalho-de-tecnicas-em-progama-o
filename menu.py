from telas import *
from persistencia import Persistencia



def menu():
    limparTela()
    print("-------- Sistema de Aluno--------")
    print("1 - Cadastrar Aluno")
    print("2 - Editar Aluno")
    print("3 - Excluir Aluno")
    print("4 - Selecionar Aluno")
    print("5 - Listar Alunos")
    print("6 - Sair")
    print("-------------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

persistencia = Persistencia()

while True:
    opcao = menu()

    if opcao == 1:
        aluno = cadastraraluno()
        persistencia.criar(aluno)
        exibirMsg("Aluno  cadastrado com sucesso!")
    elif opcao == 2:
        produto = editaraluno()
        persistencia.editar(aluno)
        exibirMsg("Aluno editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = excluiraluno()
        persistencia.excluir(id)
        exibirMsg("Aluno excluído com sucesso!")
    elif opcao == 4:
        id = selecionaraluno()
        aluno = persistencia.selecionar(id)
        if aluno == None:
            exibirMsg("Aluno não encontrado!")
        else:
            exibiraluno( aluno )
            travarTela()
    elif opcao == 5:
       alunos = persistencia.selecionar_todos()
       exibiralunos(alunos)
    elif opcao == 6 :
        
        break
