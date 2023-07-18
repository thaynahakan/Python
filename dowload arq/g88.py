#Exercício Python 88:  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
palpites = []
vezes = 1
dados = []

print(f' JOGO DO BICHO DA VIRADA; TÊY - TÊY')
quantas = int(input(f' Quantas cartelas de palpite você deseja?'))
while vezes <= quantas:

    for i in range(0,6):
        n = randint(1,99)
        if n not in dados:
            dados.append(n)

    palpites.append(dados[:])
    dados.clear()
    vezes +=1
print(f'     x-x-x SORTEANDO {quantas} JOGOS x-x-x')
for l,n in enumerate(palpites):
    print(f' A {l+1}* jogada da sorte é: {n}')
    sleep(1)

print('=-'*10, '> Boa sorte <', '-='*10)
