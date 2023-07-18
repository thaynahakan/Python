#Exercício Python082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

par = []
impar = []
lista = []
while True:
    lista.append(int(input('Digite o valor:')))
    escolha = str(input('Quer continuar?[SIM-NÃO]'))
    if escolha in 'Nn':
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print(f' A lista TOTAL É: {lista}')
print(f' a lista de números pares: {par}')
print(f' A lista de números impar: {impar}')