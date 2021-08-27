# Vamos criar um menu em Python, usando modularização.
# Vamos ver como fazer acesso a arquivos usando o Python.
# Vamos finalizar o projeto de acesso a arquivos em Python.

from opcoes import menu, opcao1, opcao2, opcao3
while True:
    opcao = menu()
    if opcao == 1:
        opcao1.pessoas_cadastradas()
    elif opcao == 2:
        opcao2.cadastrar_pessoa()
    elif opcao == 3:
        opcao3.opcao3()
        break
