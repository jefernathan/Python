# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

n = input('Digite um preço: R$')
print(f'Com 10% de aumento fica {moeda.aumentar(n, 10, True)}')
print(f'Com 10% de desconto fica {moeda.dimimuir(n, 10, True)}')
print(f'A metade é {moeda.metade(n, True)} e o dobro é {moeda.dobro(n, True)}')
