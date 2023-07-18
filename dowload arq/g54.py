# Desenvolva um programa que peça 7 idades de 7 pessoas e leia quem já é maior de idade
maior = 0
menor = 0

'''for p in range(1, 5):
    pessoas = input('Nome:')
    idade = int(input('Idade:'))
    if p == 1:
        menor = idade
        maior = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < maior:
            menor = idade

#pessoa_velha = pessoas maior
print(f' A pessoa mais velha tem {maior}')
print(f' A pessoa mais nova tem {menor}')'''


#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = []
menor = []
contador_maior = 0
contador_menor = 0
for c in range(1,8):
    ano = int(input('Ano de nascimento:'))

    atual = date.today().year
    idade = atual - ano

    if idade >= 21:
        maior.append(idade)
        contador_maior += 1

    elif idade < 21:
        menor.append(ano)
        contador_menor += 1




print(f' {contador_maior} pessoas são maiores de idade\n'
      f'segue a lista com ao ano de nascimento: {maior}')

print(f' {contador_menor} pessoas são menores de idade\n'
      f'segue a lista com ao ano de nascimento: {menor}')