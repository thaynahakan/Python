#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

print(f' Listagem Tecnica das Gostosas 2023.1')

dados = []
pessoas = []
menor = maior = 0
contador = 0
while True:
    dados.append(str(input('Nome:')).upper())
    dados.append(float(input('Peso:')))
    if contador == 0:
        menor = maior = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    contador += 1
    parar = str(input('Deseja parar o programa? [S/N]')).upper().strip()[0]
    print('--'*25)
    if parar in 'Ss':
        break

print(f' Tem {len(pessoas)} Pessoas cadastradas no sistema.')
print(f' A pessoa mais pesada tem {maior}Kg e se chama: ', end='')
for n in pessoas:
    if n[1] == maior:
        print(f'[{n[0]}]')
print(f' A pessoa mais leve pesa {menor}Kg e se chama:', end='')
for n in pessoas:
    if n[1] == menor:
        print(f'[{n[0]}]')

print('-='*25)