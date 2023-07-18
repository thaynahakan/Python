# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

numero_secredo = randint(1,10)

chute = int(input('Chute:'))

while chute != numero_secredo:
    if chute > numero_secredo:
        print('Chute maior que o número secreto')
    if chute < numero_secredo:
        print('Chute menor que o número secreto.')
    chute = int(input('Chute:'))


if chute == numero_secredo:
    print('Acertou!')


#acertou = False
# while not acertou:
# if jogador == computador
#   acertou == True