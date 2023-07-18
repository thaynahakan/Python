#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*m):
    cont = maior = 0
    for valor in m:
        print(f'{valor}, ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} Valores.')
    print(f' O maior numero é {maior}')


maior(4,5,6,3,2,8,9)
maior(2,3)



