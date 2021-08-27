# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint
from time import sleep


def maior_valor(valor):
    print('-='*25)
    maior = 0
    print(f'Analizando os {len(valor)} valores passados: ', end='')
    for x in valor:
        print(x, end=' ')
    print()
    for y in range(0, len(valor)):
        if y == 0:
            maior = valor[y]
        else:
            if maior < valor[y]:
                maior = valor[y]
    print(f'O valor {maior} foi o maior')


vezes = int(input('Quer ver o maior valor quantas vezes: '))
for x in range(0, vezes):
    numeros = []
    for y in range(0, randint(1, 10)):
        sorteado = randint(0, 10)
        if sorteado != 0:
            numeros.append(sorteado)
    maior_valor(numeros)
    sleep(1.5)
