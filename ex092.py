# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados = dict()

while True:
    dados['nome'] = str(input('Nome: '))
    dados['idade'] = date.today().year - int(input('Ano de nascimeno: '))
    carteira_de_trabalho = int(input('Carteira de trabalho [0 se não tem]: '))
    if carteira_de_trabalho == 0:
        break
    else:
        dados['carteira de trabalho'] = carteira_de_trabalho
        dados['ano de contratação'] = int(input('Ano de contratação: '))
        dados['salário'] = float(input('Salário: '))
        dados['aposentadoria'] = dados['ano de contratação'] - date.today().year + 35 + dados['idade']
        break

print('-='*30)
for k, v in dados.items():
    print(f'    - {k} tem o valor {v}')
