# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
termos_mostrar = 10

while contador < termos_mostrar:
    print(termo, end=' ➔ ')
    termo += razao
    contador += 1

    if contador == termos_mostrar:
        termos_mostrar += int(input('\nQuer mostrar mais quantos termos? '))

print(f'Foram {termos_mostrar} termos mostrados')
