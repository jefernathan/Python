# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
pares = list()
impares = list()

while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    if numero != 0:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break

print(f'Os valores digitados foram: {lista}')
print(f'Os valores pares foram: {pares}')
print(f'Os ímpares foram: {impares}')
