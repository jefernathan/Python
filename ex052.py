#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
divisores = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        print('\033[1;31m', end='')
        divisores += 1
    else:
        print('\033[0;32m', end='')
    print(x, end=' ')

print(f'\033[m,\nO {numero} possui {divisores} divisores, então ele', end='')
if divisores == 2:
    print('\033[1;32m é primo\033[m')
else:
    print('\033[1;31m não é primo\033[m')

