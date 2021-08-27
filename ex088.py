# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print('-='*20)
print(f'{"SORTEAR GAMES":^40}')
print('-='*20)
numero = int(input('Digite quantos games sortear: '))
print(f'{f"_-=-=SORTEANDO {numero} GAMES=-=-_":^40}')
sleep(0.5)
temp = []
games = []

for x in range(0, numero):
    for y in range(0, 6):
        numero_sorteado = randint(1, 61)
        if y == 0:
            temp.append(numero_sorteado)
        else:
            while numero_sorteado in temp:
                numero_sorteado = randint(1, 61)
            temp.append(numero_sorteado)
    temp.sort()
    games.append(temp[:])
    temp.clear()
    print(f'Game {x+1}: {games[x]}')
    sleep(0.5)
print('#'*35)
