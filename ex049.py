# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

multiplicando = int(input('Digite um número: '))

for multiplicador in range(1, 11):
    print(f'{multiplicando} x {multiplicador} = {multiplicando * multiplicador}')
