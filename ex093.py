# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogo = dict()
gols_partida = list()
gols_total = 0
jogo['nome'] = str(input('Nome do jogador: '))
partidas_jogadas = int(input(f'Quantas partidas {jogo["nome"]} jogou: '))

for partida in range(0, partidas_jogadas):
    gols = (int(input(f'Quantos gols na partida {partida}: ')))
    gols_total += gols
    gols_partida.append(gols)
jogo['gols'] = gols_partida
jogo['total'] = gols_total

print('-='*30)
print(jogo)
print('-='*30)
for k, v in jogo.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogo["nome"]} jogou {partidas_jogadas} partidas')
for partida in range(0, len(jogo['gols'])):
    print(f'    => Na partida {partida} fez {jogo["gols"][partida]} gols')
print(f'Foram {jogo["total"]} gols no total')
