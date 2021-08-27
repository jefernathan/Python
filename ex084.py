# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = [[], []]
pessoas = menor = maior = 0

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    if pessoas == 0:
        menor = maior = peso
        lista[0].append(nome)
        lista[1].append(nome)
    else:
        if peso <= menor:
            if menor != peso:
                lista[0].clear()
            menor = peso
            lista[0].append(nome)
        if peso >= maior:
            if maior != peso:
                lista[1].clear()
            maior = peso
            lista[1].append(nome)
    pessoas += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print(f'Foram cadastradas {pessoas} pessoas')
print(f'A pessoa mais pesada pesa {maior}kg, e se chama {lista[1]}')
print(f'A pessoa mais leve pesa {menor}kg, e se chama {lista[0]}')
