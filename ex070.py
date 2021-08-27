# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

preco_total = produtos_acima_de_1000 = produto_mais_barato = 0
nome_produto_mais_barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    preco_total += preco
    if preco >= 1000:
        produtos_acima_de_1000 += 1
    if produto_mais_barato == 0 or produto_mais_barato > preco:
        produto_mais_barato = preco
        nome_produto_mais_barato = produto
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
    
print(f'{"PRONTO":-^30}')
print(f'Preço total: R${preco_total}')
print('Produtos acima de R$1000:', produtos_acima_de_1000)
print(f'Produto mais barato: {nome_produto_mais_barato} R${produto_mais_barato}')
print('-=' * 15)
