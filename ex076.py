# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

pc_do_cev = 'Processador', 329,\
    'Memória ', 304,\
    'Placa mãe', 278,\
    'HD', 173,\
    'SSD', 224.5,\
    'Fonte', 169,\
    'Gabinete', 133,\
    'Monitor', 280,\
    'Kit teclado e mouse', 130,\
    'Windows 10 pro', 120,\
    'Antivírus', 40

print('-='*15)
print(f'{"Pc do Curso em Vídeo":^30}')
print('-='*15)

for x in range(0, len(pc_do_cev)):
    if x % 2 == 0:
        print(f'{pc_do_cev[x]:.<21}', end='')
    else:
        print(f'R${pc_do_cev[x]:>9.2f}')
print('-='*15)
