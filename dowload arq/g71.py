# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('ʕ•́ᴥ•̀ʔっ OI PUTAH ʕ•́ᴥ•̀ʔっ')
print('Bem vinda ao Banco de Quenga Durah')
valor_saque = int(input('Qual o valor que você deseja sacar? '))
print('(✿◠‿◠) ')
cedula = 50
total = valor_saque
totalced = 0

while True:
    if total >= cedula:
        total = total - cedula
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f' Receba {totalced}  cedula de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break


print(f' Obrigada por ser burrah ≧◠ᴥ◠≦')
print('Boa vida (✿◠‿◠) ')


