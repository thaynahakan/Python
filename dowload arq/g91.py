#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}

resultado = list()
print('-='*15)
print('    > ✿ ROLANDO O DADO ✿ <')
for k,v in jogo.items():
    print(f' O {k} tirou: {v}')
    sleep(1)
print('✿❀'*20)

resultado = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print(' ❀ O PÓDIO DOS DADOS GAGOS ❀')
for k,v in enumerate(resultado):
    print(f' O {k+1}* colocado foi: {v[0]}!!! que tirou {v[1]}!')
    sleep(1)
print(f'✿❀'*20)