# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc

number = float(input('Digite um número real: '))

print(f'O número {number} arredondado é', trunc(number))
