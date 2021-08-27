# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite mais um nome: ')
nome4 = input('Digite o último nome: ')
nome = [nome1, nome2, nome3, nome4]

print(choice(nome))
