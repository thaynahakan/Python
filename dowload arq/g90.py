#Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
chamada = dict()

chamada['nome'] = str(input('Nome:'))
chamada['media'] = float(input('Média:'))

if chamada['media'] >= 7:
    chamada['situacao'] = 'Aprovado'
elif 5 >= chamada['media'] < 7:
    chamada['situacao'] = 'Recuperação'
else:
    chamada['situacao'] = 'Reprovado'

for k, n in chamada.items():
    print(f' {k} é:  {n}')