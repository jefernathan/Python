#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}')

if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')
