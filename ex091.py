# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

jogadores = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}

for jogador, numero_do_dado in jogadores.items():
    print(f'{jogador} tirou {numero_do_dado}')
    sleep(0.5)
posicao = 1
print('-='*30)
for x in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'    {posicao}º lugar ficou o {x} com', end=' ')
    print(f'{jogadores[x]} pontos')
    posicao += 1
    sleep(0.5)
