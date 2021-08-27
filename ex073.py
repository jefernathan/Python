# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = 'Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio',\
        'Palmeiras', 'Corinthians', 'Red Bull Bragantino', 'Athletico', 'Santos', 'Ceará',\
        'Atlético-GO', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo'

print('= =-' * 15)
print('Os times do Brasileirão são:', times)
print('= =-' * 15)
print('Os cinco primeiros colocados são:', times[:5])
print('= =-' * 15)
print('Os últimos 4 colocados são:', times[-4:])
print('= =-' * 15)
print('Os times em ordem alfabética são:', sorted(times))
print('= =-' * 15)
print(f'O time do Palmeiras esta na {times.index("Palmeiras")+1}ª pocição.')
print('= =-' * 15)
