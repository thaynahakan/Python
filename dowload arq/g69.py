#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

maior = 0
homens = 0
mulher20 = 0

while True:

    sexo = str(input('Sexo [Masc / Fem]: ')).upper().strip() [0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [Masc / Fem]: ')).upper().strip()[0]

    idade = int(input('Idade:'))

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade >= 20:
            mulher20 += 1

    if idade >= 18:
        maior +=1

    desejo = str(input('Deseja continuar[Sim/Não]?')).upper().strip()[0]
    while desejo not in 'SN':
        desejo = str(input('Deseja continuar[Sim/Não]?')).upper().strip()[0]
    if desejo == 'N':
        print('Fim do programa')
        break

print(f' Tem {maior} pessoas maior de 18 anos\n'
      f' {homens} homens foram cadastrados\n'
      f' {mulher20} mulher tem mais de 20 anos')