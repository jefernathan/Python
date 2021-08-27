#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero, show=False):
    """

    :param numero: calcualar fatorial
    :param show: (opcional) mostrar o cálculo
    :return: resultado do fatorial
    """
    resultado = 1
    for num in range(numero, 1, -1):
        if show:
            print(num, end=' x ')
        resultado *= num
    print(f'{1} = ', end='')
    return resultado


print(fatorial(10, True))
help(fatorial)
