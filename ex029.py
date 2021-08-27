# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

Km = int(input('Digite a velocidade em Km: '))

if Km <= 80:
    print(f'{Km}Km, velocidade abaixo de 80 Km')
else:
    print(f'{Km}Km, velocidade acima de 80 Km: a muta é de: R${(Km - 80) * 7}')
