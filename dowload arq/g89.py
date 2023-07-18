#Exercício Python thon 089: Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
composta = list()
while True:
    nome = str(input('Nome:'))
    nota_1 = float(input('Nota 1:'))
    nota_2 = float(input('Nota 2:'))
    media = (nota_1 + nota_2) / 2
    composta.append([nome,[nota_1,nota_2],media])

    cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont in 'nN':
        break

print('   BOLETIM ESCOLAR   ')
print(f'{"Num":<5}{"Nome":<15}{"Media":>10}')

for p, m in enumerate(composta):
    print(f'{p:<5} {m[0]:<15} {m[2]:>10}')
print('-*'*20)

while True:
    nota = int(input('Quer saber a nota de quem?[999- encerra]'))
    if nota == 999:
        break

    if nota <= len(composta):
        print(f' A nota de {composta[nota][0]} é {composta[nota][1]}')

print(f' Obrigada por usar o sistema Bourn Bouki ;*')