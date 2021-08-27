# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input('Digite a média do aluno: '))

if aluno['Média'] >= 7:
    aluno['Situção'] = 'APROVADO'
elif aluno['Média'] >= 5:
    aluno['Situção'] = 'RECUPERAÇÃO'
else:
    aluno['Situção'] = 'REPROVADO'
for k, v in aluno.items():
    print(f'{k} é {v}')
