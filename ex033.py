# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))
menor = int()
maior = int()

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
else:
    if numero2 < numero3:
        menor = numero2
    else:
        menor = numero3

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
else:
    if numero2 > numero3:
        maior = numero2
    else:
        maior = numero3

print(f'O menor valor é {menor}')
print(f'O maior valor é o {maior}')
