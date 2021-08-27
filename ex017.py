# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Insira o cateto oposto: '))
adjacente = float(input('Agora o cateto adjacente: '))

print(f'A hipotenusa é {hypot(oposto, adjacente):.2f}')
