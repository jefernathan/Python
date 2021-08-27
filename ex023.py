# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

number = int(input('Insira um número com 4 digítos: '))

print(f'Unidade: {number // 1 % 10}')
print(f'Dezena: {number // 10 % 10}')
print(f'Centena:{number // 100 % 10}')
print(f'Milhar: {number // 1000 % 10}')
