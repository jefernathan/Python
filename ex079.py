# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print(f'Valor {valor} adicionado a lista, ', end='')
    else:
        print(f'Valor {valor} já foi adicionado a lista, ', end='')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
    
lista.sort()
print(f'Os valores digitados foram {lista}.')
