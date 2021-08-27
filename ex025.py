# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: '))

print(f'Existe a palavra Silva no seu nome? {"silva" in (nome.strip().lower())}')
