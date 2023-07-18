# Crie um programa que peça um numero e mostre o seu dobro, o seu triplo e a sua raiz quadrada

p1 = float(input("Digite o numero:"))
p2 = float(input('Digite o valor:'))

m = (p1 + p2) / 2

if m < 5.0:
    print(f'Reprovado {m}')

elif m >= 5.0 and m <= 6.9:
    print(f'Recuperação {m}')

elif m >= 7:
    print(f'Passou {m}')

