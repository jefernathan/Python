# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frase = "We're talking away", \
        "I don't know what", \
        "I'm to say I'll say it anyway", \
        "Today's another day to find you", \
        "Shying away", \
        "I'll be coming for your love, okay?",
        
for f in frase:
    print(f'\nNa frase \033[1;36m{f}\033[m temos as vogais: ', end='')
    for frase in f:
        if frase.lower() in 'aeiou':
            print(frase, end=' ')
