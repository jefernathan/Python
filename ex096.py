#  Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    print(f'A área do terreno {larg}m x {comp}m é {larg * comp:.2f}m²')


print('#'*30)
print(f'{"CALCULAR ÁREA DE TERRENO": ^30}')
print('#'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
