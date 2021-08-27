def aumentar(n=0, p=0):
    """
    Somar porcentagem
    :param n: número a ser somado
    :param p: porcentagem a ser somada
    :return: resultado
    """
    n = float(n)
    resultado = n + (n * p / 100)
    return resultado


def dimimuir(n=0, p=0):
    """
    Subtrair porcentagem
    :param n: número a ser subtraido
    :param p: porcentagem a ser subtraida
    :return: resultado
    """
    n = float(n)
    resultado = n - (n * p / 100)
    return resultado


def dobro(n=0):
    """
    Dobrar número
    :param n: número a ser dobrado
    :return: resultado
    """
    n = float(n)
    n += n
    return n


def metade(n=0):
    """
    Dividir número pela metade
    :param n: número a ser dividido
    :return: resultado da divisão
    """
    n = float(n)
    n = n / 2
    return n


def moeda(n=0, moeda='R$'):
    """
    Moeda comercial
    :param n: valor do dinheiro
    :param moeda: Tipo de moeda
    :return: valor com a meoda
    """
    return f'{moeda}{n:.2f}'.replace('.', ',')
