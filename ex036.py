# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
duracao = int(input('Duração do pagamento: '))

if casa / (12 * duracao) < (salario * 30) / 100:
    print(f'A prestação mensal é de R${casa / (12 * duracao):.2f}')
else:
    print('Você não pode comprar essa casa.')
