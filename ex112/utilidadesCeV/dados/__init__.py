def leiadinheiro(texto):
    while True:
        resultado = input(texto).strip().replace(',', '.')
        if resultado.isalpha():
            print(f'\033[;31mErro, \"{resultado}\" não é um número\033[m')
        else:
            return float(resultado)
