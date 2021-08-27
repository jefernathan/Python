#  Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(txt):
    while True:
        try:
            inteiro = int(input(txt))
        except ValueError:
            print('\033[;31mERRO, o valor digitado é inválido\033[m')
        else:
            return inteiro


def leiafloat(txt):
    while True:
        try:
            real = float(input(txt))
        except ValueError:
            print('\033[;31mERRO, o valor digitado é inválido\033[m')
        else:
            return real


numero_inteiro = leiaint('Digite um número inteiro: ')
numero_real = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {numero_inteiro} e o número real {numero_real}')
