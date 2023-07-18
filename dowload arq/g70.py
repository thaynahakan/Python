#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

total = barato = maiordemil = contador = 0
menor = ''
while True:
    nome = str(input('Nome do produto:')).strip().upper()
    preco = int(input('Valor do Produto: R$'))
    contador +=1
    total += preco

    if preco >= 1000:
        maiordemil += 1

    if contador == 1 or preco < barato:
        barato = preco
        menor = nome

    cont = str(input('Quer continuar[Sim/Não]?')).strip().upper()[0]
    if cont in 'N':
        print('Finalizando a compra...')
        break

print(f' {maiordemil} produtos custaram mais de mil reais.\n'
      f' O valor total da compra foi de {total} R$\n'
      f' {menor} foi o produto mais barato da compra')