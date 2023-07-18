# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idoso = 0
contador = 0
soma_idades = 0
for pessoa in range(1,5):
    print(f'-------{pessoa} PESSOA -------')
    nome = str(input('Nome:')).upper()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo (M - F):')).upper()
    soma_idades = soma_idades + idade




    if sexo in 'mM':
        if pessoa == 1:
            idoso = idade
    else:
        if idade > idoso:
            idoso = idade


    if sexo in 'Ff':
        if idade < 20:
            contador = contador + 1


media = soma_idades / pessoa

print(f' A maior idade do grupo dos homens é:{idoso}')
print(f' Tem {contador} mulheres com menos de 20 anos')
print(f' A média de idade do grupo é de: {media}')
