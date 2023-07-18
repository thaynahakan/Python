# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Digite o peso da {p} pessoa:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f' A pessoa mais pesada tem: {maior} Kg.')
print(f' A pessoa mais leve tem: {menor} Kg')