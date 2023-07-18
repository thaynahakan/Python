# Crie um programa que peça um numero e mostre o seu dobro, o seu triplo e a sua raiz quadrada

n = int(input("Digite o numero:"))
d = n * 2
t = n * 3
r = n **(1/2)

print(f' O nuúmero é: {n}\n Dobro: {d}\n Triplo: {t}\n Raiz Quadrada: {r:.2f}')