from alunos import*
a = Cadastra
b = Altera
c = Deletar
d = Selecionar
e = Selecionartodos
while True:
    opção = menu()
    if opção ==1:
        a.cadastraraluno(self=Cadastra)
    elif opção == 2:
        b.alteraraluno(self=Altera)
    elif opção ==3:
        c.deletaraluno(self=Deletar)
    elif  opção == 4:
        d.selecionarmatricula(self=Selecionar)
    elif opção == 5:
        e.selecionartodos(self=Selecionartodos)
        os.system('clear')
    elif opção == 6:
        print("Obrigado por usar nosso sistema... ")
        break