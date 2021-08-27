# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def ajuda(a):
    from time import sleep
    print('\033[1;;46m~'*40)
    print(f'{f"Pesquisando a função ou biblioteca {a}": ^40}')
    print('~' * 40)
    sleep(1)
    print('\033[7;47m')
    help(a)


pesquisa = ' '
while True:
    print('\033[1;;44m~'*30)
    print(f'{"Sistema de ajuda PyHelp": ^30}')
    print('~' * 30)
    pesquisa = str(input('\033[1;;45mO que pesquisar no comando help? [fim para parar]: ')).strip()
    if pesquisa == 'fim':
        break
    else:
        ajuda(pesquisa)
print('\033[m<<<FIM>>>')
