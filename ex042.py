# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

reta1 = float(input('Digite a tamanho de uma reta: '))
reta2 = float(input('Digite o tamanho de outra reta: '))
reta3 = float(input('Digite o tamanho de mais uma reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível formar um triângulo ', end='')
    if reta1 == reta2 == reta3:
        print('equilátero')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('isóscelos')
    elif reta1 != reta2 != reta3:
        print('escaleno')
