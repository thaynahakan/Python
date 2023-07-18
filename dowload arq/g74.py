#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n = []

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f' Os valores sorteados foram: {tupla}')

# for n in tuplas:  aqui fara os valores aparecerem ser estar dentro da tupla
#   print(f'{n}', end = '' )


print(f' O menor número da lista é {min(tupla)}')
print(f' O maior número da lista é {max(tupla)}')