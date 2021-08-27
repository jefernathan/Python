# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Diga o nome de um cidade: '))

print(f'Essa cidade começa com Santo? {"santo" in (cidade.lower().split())[0]}')
