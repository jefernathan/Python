def cadastrar_pessoa():
    print(f'{"-"*30}\n{"NOVO CADASTRO": ^30}\n{"-"*30}')
    pessoas = open("ex115/pessoas.txt", "a")
    temp = list()
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(';')
    while True:
        idade = input('Idade: ').strip()
        if idade.isnumeric():
            temp.append(idade)
            temp.append('\n')
            break
        else:
            print('\033[31mERRO, insira sua idade\033[m')
    pessoas.writelines(temp)
