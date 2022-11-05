import os
import json


nome_do_arquivo = "alunos.json"

def lerArquivo() -> list:
    arq = open(nome_do_arquivo,'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)

def salvar_arquivo(alunos :dict):
     arq = open(nome_do_arquivo, 'w+', encoding='utf-8')
     data = json.dumps(alunos, indent=4)
     arq.write(data)
     arq.close()

def cadastraraluno() -> dict:
    aluno = {}
    aluno['Nome'] = input("Digite o nome do Aluno: ")
    aluno['CPF'] = float(input("Digite o numero do CPF do Aluno: "))
    aluno['Matricula'] = str(input("Digite o numero da Matricula do Aluno: "))
    aluno['Endereço'] = str(input("Digite o Endereço do Aluno: "))
    aluno['Telefone'] = int(input("Digite o Numero do Aluno: "))

    alunos = lerArquivo()
    alunos.append(aluno)
    salvar_arquivo(alunos)



def alteraraluno():
    alunos = lerArquivo()
    
    cpf = float(input("Digite o CPF do aluno que deseja alterar: "))
    for aluno in alunos:
        if cpf == aluno["CPF"]:
            indexaluno = alunos.index(aluno)
            aluno["Nome"] = input("Digite o nome do Aluno: ")
            aluno["CPF"] = float(input("Digite o numero do CPF do Aluno: "))
            aluno["Matricula"] = str(input("Digite o numero da Matricula do Aluno: "))
            aluno["Endereço"] = str(input("Digite o Endereço do Aluno: "))
            aluno["Telefone"] = int(input("Digite o Numero do Aluno: "))

            alunos[indexaluno] = aluno
            salvar_arquivo(alunos)
            print('O novo CPF do Aluno e {}'.format(cpf))


def deletaraluno():   
     
    alunos = lerArquivo()
    nome_aluno = str(input("Digite o nome do aluno que deseja deletar: "))
    for aluno in alunos:
        if nome_aluno == aluno["Nome"]:
            alunos.remove(aluno)
            salvar_arquivo(alunos)
    input("Digite enter para continuar")
    os.system('clear' if os.name == "posix" else 'cls')


def selecionarmatricula():
    alunos = lerArquivo()
    matricula = str(input("Digite a matricula do Aluno que você deseja verificar: "))
    for aluno in alunos:
        if matricula == aluno['Matricula']:
             
             print(aluno)
             salvar_arquivo(alunos)

def selecionartodos():
    arq = open(nome_do_arquivo)
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)
             

def menu():
    print(15 * '-=-')
    print('1 - Cadastrar Aluno')
    print('2 - Alterar Aluno')
    print('3 - Deletar Aluno')
    print('4 - Selecionar pela Matricula')
    print('5 - Selecionar Todos')
    print('6 - Sair')
    print(15 * '-=-')
    return int(input('Escolha uma opção: '))