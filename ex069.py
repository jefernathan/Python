# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoas_mais_18 = homens_cadastrados = mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        pessoas_mais_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    
print('-=' * 20)
print(f'Foram cadastradas {pessoas_mais_18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens_cadastrados} homens.')
print(f'Tem {mulheres_menos_20} mulheres com menos de 20 anos.')
