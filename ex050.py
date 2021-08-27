# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma_dos_pares = quantidade_de_pares = 0

for x in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma_dos_pares += numero
        quantidade_de_pares += 1

print(f'A soma entre os {quantidade_de_pares} números pares é: {soma_dos_pares}')
