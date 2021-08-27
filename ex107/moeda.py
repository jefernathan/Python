def aumentar(n, p):
    """
    Somar porcentagem
    :param n: número a ser somado
    :param p: porcentagem a ser somada
    :return: resultado
    """
    n = float(n)
    resultado = n + (n * p / 100)
    return resultado


def dimimuir(n, p):
    """
    Subtrair porcentagem
    :param n: número a ser subtraido
    :param p: porcentagem a ser subtraida
    :return: resultado
    """
    n = float(n)
    resultado = n - (n * p / 100)
    return resultado


def dobro(n):
    """
    Dobrar número
    :param n: número a ser dobrado
    :return: resultado
    """
    n = float(n)
    n += n
    return n


def metade(n):
    """
    Dividir número pela metade
    :param n: número a ser dividido
    :return: resultado da divisão
    """
    n = float(n)
    n = n / 2
    return n
