# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print(f'\033[1;33m{" PAR OU ÍMPAR ":-^30}\033[m')
pontos = 0

while True:
    numero1 = int(input('Diga um número: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    numero2 = randint(0, 10)
    resultado = numero1 + numero2
    print(f'Você escolheu {numero1} e eu escolhi {numero2}, ', end='')
    if resultado % 2 == 0:
        print(f'{resultado} é par.')
        if escolha == 'P':
            print('\033[;32mVocê ganhou!\033[m')
            pontos += 1
        else:
            print('\033[;31mEu ganhei!\033[m')
            break
    else:
        print(f'{resultado} é ímpar.')
        if escolha == 'I':
            print('\033[;32mVocê ganhou!\033[m')
            pontos += 1
        else:
            print('\033[;31mEu ganhei!\033[m')
            break
        
print(f'Você ganhou {pontos} vezes seguidas.')
