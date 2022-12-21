from telas import *
from persistencia import Persistencia


def menu():
    limparTela()
    print("-------- Sistema de Cadastro de alunos --------")
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
        alunos = cadastrarAluno()
        persistencia.criar(alunos)
        exibirMsg("Produto cadastrado com sucesso!")
    elif opcao == 2:
        alunos = alteraraluno()
        persistencia.editar(alunos)
        exibirMsg("Produto editado com sucesso!")
    elif opcao == 3:
        limparTela()
        id = exibiraluno()
        persistencia.excluir(id)
        exibirMsg("Produto excluído com sucesso!")
    elif opcao == 4:
        id = selecionaraluno()
        produto = persistencia.selecionar(id)
        if produto == None:
            exibirMsg("Produto não encontrado!")
        else:
            exibiraluno(produto)
            travarTela()
    elif opcao == 5:
        produtos = persistencia.selecionar_todos()
        exibiralunos(produtos)
    elif opcao == 6:
        break
