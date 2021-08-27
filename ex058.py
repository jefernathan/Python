# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Eu pensei em um número entre 0 e 10')
numero = int(input('Tente adivinhar: '))
numero_sorteado = randint(0, 10)
tentativas = 1

while numero_sorteado != numero:
    if numero_sorteado > numero:
        numero = int(input('Mais, tente novamente: '))
    elif numero_sorteado < numero:
        numero = int(input('Menos, tente novamente: '))
    tentativas += 1

print(f'Muito bem, eu pensei no número {numero_sorteado}\nForam {tentativas} tentativas.')
