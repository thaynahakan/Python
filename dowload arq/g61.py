#Exercício Python 061: Refaça o DESAFIO 051,
# lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('       Gerador de PA')
print('=-'*15)
pa = int(input('Digite o primeiro numero da PA:'))
razao = int(input('Digite a PA que deseja:'))
contador = 1
termo =  pa

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('FIM')