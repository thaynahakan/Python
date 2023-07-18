#Exercício Python 076: Crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.


tupla = ('areia', "100.40",
        'Papel', '145.00',
         'Borracha', '2.50',
         'Caneta', '7.50')

print(f' lISTA DE COMPRAS' )
print(tupla)

for p in range(0,len(tupla)):
    if p % 2 == 0:
        print(f'{tupla[p].upper():.<20}', end='')

    if p % 2 == 1:
        print(f' R${tupla[p]: >8}')

