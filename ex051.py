# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for x in range(0, 10):
    print(termo, end=' ➔ ')
    termo += razao

print('FIM')
