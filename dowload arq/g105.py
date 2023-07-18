#Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)
#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*num,situação = False):
    """
    Função de receber notas e avaliar alunos, salvando informações no dicionário
    :param num: uma ou mais notas de alunos. Aceita várias *
    :param situação: Situação se quer ou não ver se está aprovado ou reprovado
    :return: dicionário com várias indormações sobre a situação do aluno
    """


    dicionario = dict()
    dicionario["total"] = len(num)
    dicionario["maior"] = max(num)
    dicionario["menor"] = min(num)
    dicionario["media"] = sum(num)/dicionario["total"]
    if situação:
        if dicionario["media"] >= 7:
            dicionario["situação"] = 'BOA'
        elif dicionario["media"]>= 5:
            dicionario["situação"] = 'Recuperação'
        else:
            dicionario["situação"] = 'Reprovada'
    return dicionario

resp = notas(1.3, 10 , 8.2, situação=False)
#notas(9, 8, 2, situação=True)
print(resp)
help(notas)