# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

menores = maiores = 0

for x in range(1, 8):
    nascimento = int(input(f'Digite o ano de nascimento [{x} de 7]: '))
    if nascimento > date.today().year - 18:
        menores += 1
    else:
        maiores += 1

print(f'Tem {menores} menores de idade e {maiores} maiores de idade')
