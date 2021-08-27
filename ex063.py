# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

seq = int(input('Quantos termos mostrar? '))
n1 = 0
n2 = 1

for x in range(0, seq):
    print(n1, end=' ➔ ')
    n1 = n1 + n2
    n2 = n1 - n2
    
print('FIM')
