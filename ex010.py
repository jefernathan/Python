# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quantos reais você têm? '))

print(f'Você pode comprar US${dinheiro / 5.24:.2f} ou €{dinheiro / 6.16:.2f}')
