# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

mais_peso = menos_peso = 0

for x in range(0, 5):
    peso = float(input(f'Digite o peso da {x + 1}ª pessoa: '))
    if x == 0:
        mais_peso = peso
        menos_peso = peso
    else:
        if mais_peso < peso:
            mais_peso = peso
        if menos_peso > peso:
            menos_peso = peso

print(f'A pessoa com mais peso possui {mais_peso}kg')
print(f'A pessoa com menos peso possui {menos_peso}kg')
