# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print('O tipo primitivo é: ', type(algo))
print(algo, 'é um número?', algo.isnumeric())
print(algo, 'é uma letra?', algo.isalpha())
print(algo, 'esta em maiusculo?', algo.isupper())
print(algo, 'esta em minusculo?', algo.islower())
print(algo, 'é apenas espacos?', algo.isspace())
print(algo, 'é alfanumérico?', algo.isalnum())
