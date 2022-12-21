import os
from aluno import Aluno

def cadastraraluno():
    limparTela()
    print("-------- Cadastro de Aluno --------")
    aluno = Aluno()
    aluno.setNome(input('Nome: '))
    aluno.setCpf(input('CPF: '))
    aluno.setMatricula(input('Numero da Matricula: '))

    return aluno


def editaraluno():
    limparTela()
    print("-------- Edição de Aluno --------")
    aluno = Aluno()
    aluno.setId(int(input("Td: ")))
    aluno.setNome(input('Nome: '))
    aluno.setCpf(input('CPF: '))
    aluno.setMatricula(input('Numero da Matricula: '))

    return aluno


def excluiraluno():
    print("-------- Exclusão de Aluno --------")
    limparTela()
    id = int(input('Id: '))
    return id


def selecionaraluno():
    limparTela()
    print("-------- Seleção de Aluno --------")
    id = int(input('Id: '))
    return id


def exibiraluno(aluno: Aluno):
    print("--------Aluno --------")
    print(f"Id: {aluno.getId()}")
    print(f"Nome: {aluno.getNome['nome']}")
    print(f"CPF: {aluno.getCpf['cpf']}")
    print(f"Matricula: {aluno.getMatricula['Matricula']}")


def exibiralunos(alunos):
    limparTela()
    print("----------------Aluno ----------------")
    for aluno in alunos:
        exibiralunos(alunos)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()
