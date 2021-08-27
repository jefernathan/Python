# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).lower()
frase_reverse = frase[::-1]

print(f'A frase invertida fica:\033[;36m {frase_reverse} \033[m', end='')
if frase.replace(' ', '') == frase_reverse.replace(' ', ''):
    print('portanto é um palíndromo')
else:
    print('portanto não é um palíndromo')
