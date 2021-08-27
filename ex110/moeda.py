def aumentar(n=0, p=0, formato=False):
    """
    Somar porcentagem
    :param n: número a ser somado
    :param p: porcentagem a ser somada
    :param formato: (opicional) mostrar o moeda
    :return: resultado
    """
    n = float(n)
    resultado = n + (n * p / 100)
    return moeda(resultado) if formato else resultado


def dimimuir(n=0, p=0, formato=False):
    """
    Subtrair porcentagem
    :param n: número a ser subtraido
    :param p: porcentagem a ser subtraida
    :param formato: (opicional) mostrar o moeda
    :return: resultado final
    """
    n = float(n)
    resultado = n - (n * p / 100)
    return moeda(resultado) if formato else resultado


def dobro(n=0, formato=False):
    """
    Dobrar número
    :param n: número a ser dobrado
    :param formato: (opicional) mostrar o moeda
    :return: resultado
    """
    n = float(n)
    n += n
    return moeda(n) if formato else n


def metade(n=0, formato=False):
    """
    Dividir número pela metade
    :param n: número a ser dividido
    :param formato: (opicional) mostrar o moeda
    :return: resultado da divisão
    """
    n = float(n)
    n = n / 2
    return moeda(n) if formato else n


def moeda(n=0, moeda='R$'):
    """
    Moeda comercial
    :param n: valor do dinheiro
    :param moeda: Tipo de moeda
    :return: valor com a meoda
    """
    n = float(n)
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, aument=10, dimin=10):
    print('-'*24)
    print(f'{"RESUMO": ^24}')
    print('-'*24)
    print(f'{"Preço analizado:": <17}{moeda(n)}')
    print(f'{f"Mais {aument}%:": <17}{aumentar(n, aument, True)}')
    print(f'{f"Menos {dimin}%:": <17}{dimimuir(n, dimin, True)}')
    print(f'{"Metade:": <17}{metade(n, True)}')
    print(f'{"Dobro:": <17}{dobro(n, True)}')
    print('-'*24)
