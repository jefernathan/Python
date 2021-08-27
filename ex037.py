# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número: '))
print('''[1] para binário
[2] para octal
[3] para hexadecimal''')
escolha = int(input('Escolha entre 1, 2 e 3: '))

if escolha == 1:
    print(f'O número {numero} em valor binário fica: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} em valoor octal fica: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O número {numero} em valor hexadecimal fica: {hex(numero)[2:]}')
else:
    print('Número invalido.')
