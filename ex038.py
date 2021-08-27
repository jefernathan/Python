# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))

if numero1 > numero2:
    print('O primeiro número possui o valor maior.')
elif numero1 < numero2:
    print('O segundo número possui o valor maior.')
else:
    print('Ambos números têm o mesmo valor.')
