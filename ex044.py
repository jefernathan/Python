# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(f'\033[1;36m{" GETECH INFORMÁTICA ":-^40}\033[m')

valor = float(input('Digite o valor a pagar: R$'))
pagamento = int(input('''
    Digite 0 para pagar à vista.
    Digite 1 para pagar no cartão.
    Digite 2 para pagar 2x no cartão.
    Digite 3 para pagar 3x ou mais no cartão.
    
Selecione o método de pagamento: '''))
if pagamento == 0:
    print(f'Total a pagar: R${valor - (valor * 10 / 100):.2f}')
elif pagamento == 1:
    print(f'Total a pagar: R${valor - (valor * 5 / 100):.2f}')
elif pagamento == 2:
    print(f'Total a pagar: R${valor:.2f}')
elif pagamento == 3:
    print(f'Total a pagar: R${valor + (valor * 20 / 100):.2f}')
