# Desenvolva um programa que leia se o numero é primo ou não

num = int(input('Digite o numero: '))
acumulador = 0

for c in range(1, num+1):
        if num % c == 0:
                acumulador += 1


if acumulador == 2:
        print(f'{num} é um número primo')
elif acumulador > 2:
        print(f'{num} não é um número primo')

