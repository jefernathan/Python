# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(n, g):
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gol(s)')


nome = input('Nome do jogador: ')
gols = input('O jogador fez quantos gols? ')
ficha(nome, gols)
