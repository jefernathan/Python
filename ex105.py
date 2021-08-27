# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*n, sit=True):
    """
    Informações das notas do aluno
    :param n: notas que serão recebidas
    :param sit: (opcional) mostrar o situação do aluno
    :return: retorna um dicionário com quantidade de notas, maior nota, menor nota, média e a situação(opcional)
    """
    nota = dict()
    nota['total'] = len(n)
    soma = 0
    for x in n:
        if x == n[0]:
            nota['maior'] = x
            nota['menor'] = x
        else:
            if x > nota['maior']:
                nota['maior'] = x
            if x < nota['menor']:
                nota['menor'] = x
        soma += x
    nota['media'] = soma / nota['total']
    if sit:
        if nota['media'] >= 7:
            nota['situacao'] = 'APROVADO'
        elif nota['media'] >= 5:
            nota['situacao'] = 'RECUPERAÇÃO'
        else:
            nota['situacao'] = 'REPROVADO'
    return nota


print(notas(7, 5, 10, 8, 9))
