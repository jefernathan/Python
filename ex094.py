# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoa = dict()
todas_pessoas = list()

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Inválido, tente novamente [M/F]: ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    todas_pessoas.append(pessoa)
    pessoa = dict()

    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Inválido, quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Foram {len(todas_pessoas)} pessoas cadastradas')

print('A média de idade foi de ', end='')
idade_total = 0
for x in range(0, len(todas_pessoas)):
    idade_total += todas_pessoas[x]['idade']
media_idade = idade_total / len(todas_pessoas)
print(f'{media_idade:.2f}')

print('As mulheres cadastradas foram ', end='')
for y in range(0, len(todas_pessoas)):
    if todas_pessoas[y]['sexo'] == 'F':
        print(todas_pessoas[y]['nome'], end=' ')

print('\nAs pessoas com idade acima da média são ', end='')
for z in range(0, len(todas_pessoas)):
    if todas_pessoas[z]['idade'] > media_idade:
        print(todas_pessoas[z]['nome'])
