#Exercício Python 096: Faça um programa que tenha uma função chamada área(),
#que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def funcao(b,h):
    area = b * h
    print(f' A área do retângulo de base {b} e altura {h}, é de {area}.')


b = int(input('Base:'))
h = int(input('Altura:'))
funcao(b,h)