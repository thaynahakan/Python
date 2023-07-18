# Desenvolva um programa que leia o primeiro termo de uma PA e a razão. No final mostre os 10 primeiros termos
#Dessa progressão.

num_inicial = int(input('Digite o primeiro termo da sua progressão:'))
razao = int(input('Digite a razão dessa PA:'))
final = int(input('Digite quantos números quer exibir:'))

ultimo = num_inicial + (final-1) * razao
ultimo = ultimo + 1

for var in range(num_inicial, ultimo, razao):
        print(var)

print(f' Você quer uma Progressão Aritimética do {num_inicial} com a razão de {razao}, a lista será: {var}')