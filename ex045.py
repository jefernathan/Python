#  Crie um programa que faça o computador jogar Jokenpô com você.

from math import e
from random import choice
from time import sleep

print('Vamos jogar jokempô!')
escolha = str(input('Pedra, papel ou tesoura? ')).lower().strip()
sleep(0.5)
print('JO...')
sleep(1)
print('KÊM...')
sleep(1)
print('PO...')
sleep(1)

jogadas_possíveis = ['pedra', 'papel', 'tesoura']
jogada = choice(jogadas_possíveis)

if escolha == jogada:
    print(f'Também escolhi {escolha}, empatamos')
else:
    if jogada == 'pedra' and escolha == 'papel':
        print('Papel embrulha pedra, VOCÊ GANHOU!')
    elif jogada == 'pedra' and escolha == 'tesoura':
        print('Pedra quebra tesoura, não foi dessa vez :(')
    elif jogada == 'papel' and escolha == 'pedra':
        print('Papel embrulha pedra, não foi dessa vez :(')
    elif jogada == 'papel' and escolha == 'tesoura':
        print('Tesoura corta papel, VOCÊ GANHOU!')
    elif jogada == 'tesoura' and escolha == 'pedra':
        print('Pedra quebra tesoura, VOCÊ GANHOU!')
    elif jogada == 'tesoura' and escolha == 'papel':
        print('Tesoura corta papel, não foi dessa vez :(')
