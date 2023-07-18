# Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares

acumulador = 0
contador = 0

for c in range(6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        acumulador = acumulador + n
        contador = contador + 1
print(f'a soma dos valores pares é: {acumulador}, você digitou {contador} números pares.')

