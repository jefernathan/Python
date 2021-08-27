# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
escolha = 0

while True:
    escolha = int(input('''    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novo número
    5 - Finalizar
>>>>Escolha uma opção: '''))
    if escolha == 1:
        print(f'A soma entre {numero1} + {numero2} é igual a {numero1 + numero2}')
    elif escolha == 2:
        print(f'A multiplicação entre {numero1} x {numero2} é igual a {numero1 * numero2}')
    elif escolha == 3:
        if numero1 > numero2:
            print(numero1, end=' ')
        else:
            print(numero2, end=' ')
        print('é o maior número.')
    elif escolha == 4:
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
    elif escolha == 5:
        print('Finalizado')
        exit()
    else:
        print('Opção inválida')
    print('=-='*10)
    sleep(2)
