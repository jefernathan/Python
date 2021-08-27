#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números gerados foram: {numeros}')
print('O maior número foi: ', end='')
print(int(max(numeros)))
print('O menor número foi: ', end='')
print(int(min(numeros)))
