# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(frase):
    print('~' * (len(frase) + 4))
    print(f'{frase: ^{len(frase) + 4}}')
    print('~' * (len(frase) + 4))


escreva(str(input('Digte algo: ')))
