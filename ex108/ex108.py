# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

n = input('Digite um preço: R$')
print(f'Com 10% de aumento fica {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'Com 10% de desconto fica {moeda.moeda(moeda.dimimuir(n, 10))}')
print(f'A metade é {moeda.moeda(moeda.metade(n))} e o dobro é {moeda.moeda(moeda.dobro(n))}')
