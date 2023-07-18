# Crie um programa que peça um numero e mostre o seu dobro, o seu triplo e a sua raiz quadrada

m = int(input("Digite a tabuada:"))

k = 0
while k <= 9:
    k = k + 1
    tb = m * k
    print(f'{m} X {k} = {tb}')

