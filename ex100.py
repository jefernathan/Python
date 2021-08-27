#  Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
numeros = []


def sorteia():
    for x in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteado 5 valores: {numeros}')


def soma_par(n):
    soma_dos_pares = 0
    for x in n:
        if x % 2 == 0:
            soma_dos_pares += x
    print(f'A soma dos pares é {soma_dos_pares}')


sorteia()
soma_par(numeros)
