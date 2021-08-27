# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = menor = 0

for x in range(0, 5):
    lista.append(int(input(f'Digite o número da posição {x}: ')))
    if x == 0:
        maior = menor = lista[x]
    else:
        if maior <= lista[x]:
            maior = lista[x]
        if menor >= lista[x]:
            menor = lista[x]

print(f'Você digitou os números: {lista}')
print(f'O maior número foi {maior} na posição', end=' ')
for x, y in enumerate(lista):
    if y == maior:
        print(f'{x}', end='... ')
print(f'\nO menor número foi {menor} na posição', end=' ')
for x, y in enumerate(lista):
    if y == menor:
        print(f'{x}', end='... ')
