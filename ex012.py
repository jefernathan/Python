# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço atual? '))

print(f'O preço com 5% de desconto é R${preco - preco * (5 / 100)}')
