#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco
# valores numéricos e cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista = []

for n in range(1,6):
    valores = int(input('Digite o valor:'))
    lista.append(valores)

    for c, v in enumerate(lista):
        print(f'A lista ficou:\n'
            f' Na posição {n} o valor {v} na lista {lista}')
