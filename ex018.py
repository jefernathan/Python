# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Insira o ângulo: '))

print(f'O seno é {sin(radians(angulo)):.2f}')
print(f'O cosseno é {cos(radians(angulo)):.2f}')
print(f'A tangente é {tan(radians(angulo)):.2f}')
