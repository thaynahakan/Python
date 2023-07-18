#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print('=-'*10)
print(' -> Calcule a média das avaliações! <- ')

resposta = 'SIM'
contador_total = 0
soma = media = maior = menor = 0

while resposta == 'SIM':
    n = int(input('Digite a nota:'))
    contador_total += 1
    soma += n

    if contador_total == 1:
        maior = menor = contador_total
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Deseja continuar [SIM ; NÃO]?')).upper().strip()



media = soma / contador_total
print(f' Você registrou {contador_total} números, e a soma deles é {soma}.')
print(f' A média dos valores é {media}')
print(f'O maior número é: {maior} e o menor é {menor}')