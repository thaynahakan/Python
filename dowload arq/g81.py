#Exercício Python Exercício Python 081: Crie um programa que vai ler vários números
# e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.  -
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista. -

numeros = []
contador = 0
cinco = 0

while True:
    numeros.append(int(input('Digite um número:')))
    contador += 1

    parar = input('Deseja parar? [SIM- NÃO]').upper().strip()[0]

    if parar == 'S':
        break

numeros.sort(reverse= True)
print(f' A lista de números em ordem decrescente é: {numeros}')
print(f' Tivemos {contador} números digitados.')

if 5 in numeros:
    print(f' Na lista tivemos citação do número 5.')