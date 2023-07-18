#Exercício Python 087: Aprimore o desafio anterior,
#mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
#Exercício Python 087: Aprimore o desafio anterior,
#mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
somapar = 0
terceira = maior = soma = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
print(f' ✿ TABELA DO JOGO DO BICHO ✿ ')
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f' Digite um valor para [{l},{c}]:'))
        soma += matriz[l][c]
        if matriz[l][c] %2 == 0:
            somapar += matriz[l][c]

print('-✿'*15)

for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0,3):
    terceira += matriz[l][2]
    for c in range(0,3):
       if c == 0:
           maior = matriz[1][c]
       else:
           if matriz[1][c] > maior:
               maior = matriz[1][c]

print('*✿'*15)
print(f' Os valores pares dessa matriz, somados são o total de: {somapar}.')
print(f' O Valor mais alto da segunda linha é {maior}.')
print(f' A soma de todos os valores da matriz é de {soma}.')
print(f' A soma da terceira coluna é de {terceira}.')