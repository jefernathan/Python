def pessoas_cadastradas():
    print(f'{"-"*30}\n{"PESSOAS CADASTRADAS": ^30}\n{"-"*30}')
    try:
        pessoas = open("ex115/pessoas.txt", "r")
    except FileNotFoundError:
        print('\033[31mNão a pessoas cadastradas\033[m')
    else:
        print(f'{"Nome": <20}{" idade"}\n{"-"*30}')
        for linha in pessoas:
            info = linha.split(';')
            info[1] = info[1].replace('\n', '')
            print(f'{info[0]: <20}{info[1]:>3} anos')
