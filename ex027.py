# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).strip().split()

print(f'{nome[0]} {nome[len(nome)-1]}')
