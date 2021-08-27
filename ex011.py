# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual é a altura? '))
largura = float(input('Qual é a largura?'))

print(f'Para pintar a parede você precisára de {(altura * largura) / 2} litros de tinta')
