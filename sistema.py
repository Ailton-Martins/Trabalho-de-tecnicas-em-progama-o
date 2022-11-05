from alunos import*

while True:
    opção = menu()
    if opção ==1:
        cadastraraluno()
    elif opção == 2:
        alteraraluno()
    elif opção ==3:
        deletaraluno()
    elif  opção == 4:
        selecionarmatricula()
    elif opção == 5:
        selecionartodos()
        os.system('clear')
    elif opção == 6:
        break              

 



