#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
quantidade = 0
inteiro = int(input('Digite um número[999 é a condição de parada]:'))


while inteiro != 999:
    soma += inteiro
    quantidade += 1
    inteiro = int(input('Digite um número[999 é a condição de parada]:'))
print(f' A quantidade de números digitada foi de {quantidade} e a soma entre eles é {soma}')