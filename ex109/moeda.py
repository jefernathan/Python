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
