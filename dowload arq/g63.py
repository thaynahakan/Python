#Exercício Python 63: Escreva um programa que leia um número N inteiro
#qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

t1 = 0
t2 = 1
contador = 3
n = int(input('QUANTOS NÚMEROS VOCÊ QUER VER?'))
print(f'{t1} -> {t2}' ,end='')
while contador <= n:
    t3 = t1 + t2
    print(f'{t3}',end='')
print('fim')