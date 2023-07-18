#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
mai = men = 0
#while contador < 5:
#    valor = int(input('Digite a Nota:'))
#    numeros.append(valor)
#    contador += 1

#    if contador == 1:
#        maior = menor = valor
#        contador+=1
 #   else:
#        if valor > maior:
#            maior = valor

#        if valor < menor:
#            menor = valor

#print(f' O maior número é {maior}')
#print(f' O menor número é {menor}')
#print(f'  lista criada foi {numeros}')
for contador in range (0,5):
    numeros.append(int(input("Digite um número:")))

    if contador == 0:
        mai = men = numeros[contador]
    else:
        if numeros[contador] > mai:
            mai = numeros[contador]
        if numeros[contador] < men:
            men = numeros[contador]
print('-='*30)
print(f' A lista digitada é a seguinte:')
print(f' O maior valor digitado foi {mai} na posição ', end='')
for v,l in enumerate(numeros):
    if l == mai:
        print(f'{v}...', end='')
print(F' O menor valor digitado foi {men} na posição...', end='')
for v,l in enumerate(numeros):
    if l == men:
        print(f'{v}...', end='')



print('-='*30)