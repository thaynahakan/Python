#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('Digite um número de 0 - 20:'))
    if numero <= 0 or numero > 20:
        print('Numero inválido, tente novamente...')
        numero = int(input('Digite um número de 0 - 20:'))

    print(f' {numero} por extenso é {extenso[numero]}')
    continuar = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        print('Finalizando o programa...')
        break


