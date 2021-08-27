# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()

for x in range(0, 5):
    valor = int(input('Digite um valor: '))
    if x == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'Valor {valor} foi adicionado ao final da lista')
    else:
        y = 0
        while y < len(lista):
            if valor <= lista[y]:
                lista.insert(y, valor)
                print(f'Valor {valor} adicionado a pocição {y} da lista')
                break
            y += 1

print('Lista:', lista)
