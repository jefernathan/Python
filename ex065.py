# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = quantidade = 0
continuar = 's'

while continuar == 's':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    continuar = str(input('Quer continuar [S/N]? ')).lower().strip()[0]
    
print(f'Você digitou {quantidade} números e a média deles é {soma / quantidade}')
