#Exercício Python 86: Crie um programa que declare uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
print(f' ✿ TABELA DO JOGO DO BICHO ✿ ')
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f' Digite um valor para [{l},{c}]:'))

print('-✿'*15)

for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('*✿'*15)
print(matriz)