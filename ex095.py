# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas que {jogador["nome"]} jogou: '))
    jogador['gols'] = list()
    for partida in range(0, jogador['partidas']):
        jogador['gols'].append(int(input(f'    Quantos gols na partida {partida}: ')))
    jogadores.append(jogador)
    jogador = dict()
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('=-'*20)
print(f'{"N"} {"Jogador": <10}{"Gols"}{"Partidas": >10}')
print('=-'*20)
for x in range(0, len(jogadores)):
    print(f'{x} {jogadores[x]["nome"]: <10} {jogadores[x]["gols"]} {jogadores[x]["partidas"]: >10}')
print('=-'*20)

while True:
    dados = int(input('Mostrar dados de qual jogador? [999 para parar]: '))
    while dados not in range(0, len(jogadores)) and dados != 999:
        dados = int(input('Dado inválido, mostrar dados de qual jogador? [999 para parar]: '))
    if dados == 999:
        break
    else:
        print(f'Os dados de {jogadores[dados]["nome"]}:')
        for x in range(0, len(jogadores[dados]['gols'])):
            print(f'    - Na partida {x} foram {jogadores[dados]["gols"][x]} gols')
print('<<<FINALIZADO>>>')
