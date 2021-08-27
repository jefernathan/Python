def menu():
    print(f'{"-"*30}\n{"MENU PRINCIPAL": ^30}\n{"-"*30}')
    print('''\033[33m 1- \033[35mVer pessoas cadastradas
\033[33m 2- \033[35mCadastrar nova pessoa
\033[33m 3- \033[35mSair do sistema\033[m''')
    print('-'*30)
    while True:
        try:
            retorno = int(input('Escolha uma opção: '))
        except ValueError:
            print('\033[31mErro, o valor digitado não é um número\033[m')
        else:
            if retorno in (1, 2, 3):
                return retorno
            else:
                print('\033[31mErro, escolha uma opção valida\033[m')
