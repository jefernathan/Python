# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Insira um nome: '))

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nome.split()[0]))
