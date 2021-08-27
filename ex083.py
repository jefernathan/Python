# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite uma expressão: '))
parenteses = 0

for x in expressao:
    if x == '(':
        parenteses += 1
    elif x == ')':
        if parenteses > 0:
            parenteses -= 1
        else:
            parenteses += 1
            break

if parenteses == 0:
    print('Sua expressão esta \033[;32mválida')
else:
    print('Sua expressão esta \033[;31minválida')
