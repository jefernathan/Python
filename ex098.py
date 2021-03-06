# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f:
        for x in range(i, f - p, -p):
            print(x, end=' ')
            sleep(0.25)
        print()
    else:
        for y in range(i, f + p, p):
            print(y, end=' ')
            sleep(0.25)
        print()


contador(1, 10, 1)
sleep(0.5)
contador(10, 0, 2)
sleep(0.5)
print('Agora você: ')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
