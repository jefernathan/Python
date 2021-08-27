# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()

print(f'Essa frase possui {frase.count("a")} letras \"A\"')
print(f'O \"A\" aparece primeiramente na posição {frase.find("a")} e e por último na posição {frase.rfind("a")}')
