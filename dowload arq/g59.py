# Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

num_1 = int(input('Digite um valor:'))
num_2 = int(input('Digite um valor:'))
operacao = 0

while operacao != 5:
    print('''Dentre as operações:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa.''')
    operacao = int(input('>>>>Escolha pelo número a desejada:'))


    if operacao == 1:
        soma = num_1 + num_2
        print(f'A soma dos numeros {num_1} + {num_2} = {soma}')

    elif operacao == 2:
        multiplicar = num_1 * num_2
        print(f' A multiplicação de {num_1} X {num_2} = {multiplicar}')

    elif operacao == 3:
        if num_1 > num_2:
            maior = num_1
        elif num_2 > num_1:
            maior = num_2
        print(f' O maior é: {maior}')

    elif operacao == 4:
        print(f' Escolha novos números...')
        num_1 = int(input('Digite um valor:'))
        num_2 = int(input('Digite um valor:'))

    elif operacao == 5:
        print('Fechar programa, good bye!')
    else:
        print('Opção inválida')
    print('=-'*20)






