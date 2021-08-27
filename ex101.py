# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(n):
    from datetime import date
    global idade
    idade = date.today().year - n
    if 18 <= idade < 70:
        return 'OBRIGATÓRIO'
    elif 16 <= idade or n >= 70:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


idade = int()
nascimento = int(input('Em que ano você nasceu? '))
voto = voto(nascimento)
print(f'Com {idade} anos o voto é {voto}')
