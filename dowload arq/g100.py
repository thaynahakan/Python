#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(numeros):
    print(f' Vamos sortear seus números da mega sena!')
    for i in range(1,6):
        n = randint(1, 10)
        numeros.append(n)
        print(f'{n} ',end='')
        sleep(0.3)
    print(f'.')
def somapar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'somando os valores pares da lista {numeros}, temos {soma} é a soma dos números pares dessa lista.')


numeros = list()
sorteia(numeros)
somapar(numeros)