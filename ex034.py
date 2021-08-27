#  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário: '))

if salario <= 1250:
    print(f'Com mais 15% o salário fica R${salario + (salario * 15 / 100)}')
else:
    print(f'Com mais 10% o salário fica R${salario + (salario * 10 / 100)}')
