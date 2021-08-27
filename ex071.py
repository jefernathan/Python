# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite um valor: '))
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0

while True:
    while valor >= 50:
        cedulas_50 += 1
        valor -= 50
    while valor >= 20:
        cedulas_20 += 1
        valor -= 20
    while valor >= 10:
        cedulas_10 += 1
        valor -= 10
    while valor >= 1:
        cedulas_1 += 1
        valor -= 1
    break

print(f'''{cedulas_50} cédulas de R$50
{cedulas_20} cédulas de R$20
{cedulas_10} cédulas de R$10
{cedulas_1} cédulas de R$1''')
