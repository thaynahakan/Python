#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def contar(i,f,p):
    print('-'* 20)
    print('    Contador py.')
    if f < i:
        for c in range(i, f-2, -p):
            print(f'{c} ', end='')
            sleep(0.3)
        print()
    else:
        for c in range(i, f, p):
            print(f'{c} ', end='')
            sleep(0.1)
        print()


contar(1,11,1)
contar(10,0,2)
print('Agora é a sua vez! Pesonalize sua contagem')
i = int(input('Inicio:'))
f = int(input('Fim:   '))
p = int(input('Pulando:'))
contar(i,f+1,p)