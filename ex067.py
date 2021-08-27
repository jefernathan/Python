# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-=' * 15)
    multiplicando = int(input('Digite um número: '))
    print('-=' * 15)
    if multiplicando < 0:
        break
    for multiplicador in range(1, 11):
        print(f'{multiplicando} x {multiplicador} = {multiplicando * multiplicador}')
        
print('ENCERRADO')
