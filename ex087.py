# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        numero = int(input(f'Digite um número para [{linha}, {coluna}]: '))
        lista[linha][coluna] = numero
        if numero % 2 == 0:
            pares += numero
        if linha == 1 and 0 == coluna or linha == 1 and numero > maior:
            maior = numero

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{lista[linha][coluna]:^5}]', end=' ')
    print()

print('-='*20)
print(f'A soma de todos números pares é igual a {pares}')
print(f'A soma dos valores da terceira coluna é igual a {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é o {maior}')
