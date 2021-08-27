# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Insira o tamanho da reta: '))
reta2 = float(input('Insira o tamanho de outra reta: '))
reta3 = float(input('Insira o valor de mais uma reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo')
