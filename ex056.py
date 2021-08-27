#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media_de_idade = idade_do_homem_mais_velho = mulheres_com_menos_de_vinte = 0
nome_do_homem_mais_velho = ' '

for x in range(0, 4):
    print('_'*15)
    print(f'{x + 1}ª pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower().strip()[0]
    media_de_idade += idade
    if idade_do_homem_mais_velho < idade and sexo == 'm':
        idade_do_homem_mais_velho = idade
        nome_do_homem_mais_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres_com_menos_de_vinte += 1
        
print(f'A média de idade do gupo é de {media_de_idade / 4} anos.')
print(f'O nome do homem mais velho é {nome_do_homem_mais_velho} e ele possui {idade_do_homem_mais_velho} anos.')
print(f'Tem {mulheres_com_menos_de_vinte} mulheres com menos de 20 anos no grupo.')
