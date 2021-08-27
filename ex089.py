# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
temp = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    temp.append(nome), temp.append(nota1), temp.append(nota2)
    alunos.append(temp[:])
    temp.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-='*20)
print(f'{"Nº Nome": <15}{"Média"}')
for x in range(0, len(alunos)):
    print(f'{x} {alunos[x][0]: <15}{(alunos[x][1] + alunos[x][2])/2}')
while True:
    escolha = int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if escolha == 999:
        break
    elif escolha >= len(alunos):
        print('\033[;31mAluno não cadastrado, tente novamente\033[m')
    else:
        print(f'\nAluno: {alunos[escolha][0]}\n1ª nota: {alunos[escolha][1]}\n2ª nota: {alunos[escolha][2]}\n')
print('FINALIZADO')
