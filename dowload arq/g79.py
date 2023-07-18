#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

lista = []
contador = 0
while True:
    valor =int(input('Valor:'))
    contador += 1

    if contador == 1:
        lista.append(valor)
    else:
        if valor == valor in lista:
            print('Esse valor ja foi cadastrado')
            valor = int(input('Valor:'))
        if valor not in lista:
            lista.append(valor)

    if valor in lista:
        print(f'Digite outro valor')
    quer = input('Quer continuar?[Sim/ Não]').upper().strip()[0]

    if quer in 'N':
        break

print('-='*30)
lista.sort()
print(f' Os valores digitados foram: {lista}')


