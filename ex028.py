# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('\033[;33m=-'*20)
print(f'{"Tente me adivinhar": ^40}')
print('=-'*20)

numero1 = int(input('\033[mPense em número entre 0 e 5: '))
numero2 = randint(0, 5)

print('\033[33mProcessando...')
sleep(3)

if numero1 == numero2:
    print(f'\033[32mPARABÉNS\033[m')
else:
    print(f'\033[31mNão foi dessa vez\033[m')

print(f'Eu pensei no número {numero2}')
