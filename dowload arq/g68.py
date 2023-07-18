#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

impar = 'iI'
par = 'pP'
jogador = 0
venceu = 0
perdeu = 0
computador = randint(1,10)


while True:
    computador = randint(0, 11)
    parim = str(input('Par ou Impar?')).upper().strip()[0]
    jogue = int(input('Digite um número:'))
    print(f'Você jogou {jogue}, pediu {parim}. O computador jogou: {computador}.')

    resultado = jogue + computador

    if parim == 'P':
        if resultado % 2 == 0:
            venceu +=1
            print(f'{resultado} é Par, você venceu.')
        else:
            print(f' {resultado} você perdeu.')
            break

    if parim == 'I':
        if resultado % 2 == 1:
            venceu += 1
            print(f'{resultado} é ímpar, você venceu.')

        else:
            print(f'{resultado} é par e você perdeu.')
            break
print(f' Você venceu {venceu} vezes o computador antes de perder.')