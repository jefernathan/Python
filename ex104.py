#  Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaint(leia):
    num = ' '
    while not num.isnumeric():
        num = input(leia)
        if not num.isnumeric():
            print('\033[;31mERRO, TENTE NOVAMENTE\033[m')
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o numero {n}')
