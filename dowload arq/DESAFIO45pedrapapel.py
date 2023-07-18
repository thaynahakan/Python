from random import randint
from time import sleep
print('''Escolha a forma de Jogar.
[0] pedra
[1] papel
[2] tesoura''')

item = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)


print('-=' * 11)
eu = int(input("escolha:"))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print(f' O computador escolheu: {item[computador]}')
print(f' Eu escolhi: {item[eu]}')

if eu == 1 and computador ==1:
    print('Empate')
elif eu == 1 and computador == 2:
    print('JOGADOR PERDEU')
elif eu == 1 and computador == 0:
    print('JOGADOR VENCEU')


if eu == 0 and computador == 0:
    print('Empate')
elif eu == 0 and computador == 1:
    print('JOGADOR PERDEU')
elif eu == 0 and computador == 2:
    print('JOGADOR VENCEU')


if eu == 2 and computador == 0:
    print('JOGADOR PERDEU')
elif eu == 2 and computador == 1:
    print('JOGADOR VENCEU')
elif eu == 2 and computador == 2:
    print('Empatou')

print('-=' * 11)