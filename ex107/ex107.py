# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

n = input('Digite um preço: R$')
print(f'Com 10% de aumento fica R${moeda.aumentar(n, 10)}')
print(f'Com 10% de desconto fica R${moeda.dimimuir(n, 10)}')
print(f'A metade é R${moeda.metade(n):.2f} e o dobro é R${moeda.dobro(n):.2f}')
