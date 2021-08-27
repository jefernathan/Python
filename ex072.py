# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros_por_extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', \
    'seis', 'sete', 'oito', 'nove', 'dez', \
    'onze', 'doze', 'treze', 'quartoze', 'quinze', \
    'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente.', end=' ')
    print('Você digitou o número', numeros_por_extenso[numero])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
    
print('Finalizado')
