import os
from Alunos import Alunos


def cadastrarAluno() -> Alunos:
    limparTela()
    print("-------- Cadastro de Aluno --------")
    aluno = Alunos()
    aluno.setNome(input('Digite o nome do aluno: '))
    aluno.setCPF(float(input('Digite o cpf do aluno: ')))
    aluno.setMatricula(int(input('Digite a matricula do aluno: ')))
    aluno.setEndereço(str(input('Digite o endereço do aluno: ')))
    aluno.setTelefone(str(input('Digite o Telefone do aluno: ')))

    return aluno


def alteraraluno() -> Alunos:
    limparTela()
    print("-------- Alteração do aluno --------")
    aluno = Alunos()
    aluno.setNome(input('Digite o nome do aluno: '))
    aluno.setCPF(float(input('Digite o cpf do aluno: ')))
    aluno.setMatricula(int(input('Digite a matricula do aluno: ')))
    aluno.setEndereço(str(input('Digite o endereço do aluno: ')))
    aluno.setTelefone(str(input('Digite o Telefone do aluno: ')))

    return aluno


def excluiraluno():
    print("-------- Exclusão do aluno --------")
    limparTela()
    id = int(input('Matricla do aluno que deseja deletar: '))
    return id


def selecionaraluno():
    limparTela()
    print("-------- Seleção do Aluno --------")
    id = int(input('Digite o CPF do aluno que deseja selecionar: '))
    return id


def exibiraluno(aluno: Alunos):
    print("-------- Aluno --------")
    print(f"Nome: {aluno.getNome()}")
    print(f"CPF: {aluno.getCPF()}")
    print(f"Matricula: {aluno.getMatricula()}")
    print(f"Endereço: {aluno.getEndereço()}")
    print(f"Telefone: {aluno.getTelefone()}")


def exibiralunos(aluno):
    limparTela()
    print("---------------- Alunos ----------------")
    for aluno in aluno:
        exibiraluno(aluno)
    travarTela()


def limparTela():
    os.system('clear' if os.name == 'posix' else 'cls')


def travarTela():
    input('Pressione ENTER para continuar...')


def exibirMsg(msg):
    print(msg)
    travarTela()
