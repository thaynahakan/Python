#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
valores =[[],[]]
valor = []
for c in range(1,8):
    valor = int(input('Digite o Valor:'))
    if valor % 2 == 0:
        valores[1].append(valor)
    else:
        valores[0].append(valor)

valores[0].sort()
valores[1].sort()
valores.sort()
print(f'A lista completa é:{valores}')
print(f' Apenas pares {valores[1]}')
print(f' Apenas ímpares {valores[0]}')