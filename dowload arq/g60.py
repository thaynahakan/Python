#Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial


print('Digite o número que você quer o Fatorial:')
n = int(input('Numero:'))
print(f'O fatorial de {n} é: {factorial(n)}')


