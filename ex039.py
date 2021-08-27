# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

nascimento = int(input('Insira o ano de seu nascimento: '))
idade = date.today().year - nascimento
print('''[1] para masculino
[2] para feminino''')
escolha = int(input('Digite seu gênero: '))

if escolha == 1:
    if idade < 18:
        print(f'Faltam {18 - idade} anos para você se alistar')
    elif idade == 18:
        print('Já é a hora de você se alistar')
    else:
        print(f'Já se passaram {idade - 18} anos para você se alistar')
elif escolha == 2:
    print('Você não precisa se alistar')
else:
    print('Número errado')
