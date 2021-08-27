# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km = int(input('Quantos km foram pecorridos? '))
dias = int(input('E em quantos dias? '))

print(f'O total a pagar é R${(Km * 0.15) + (dias * 60)}')
