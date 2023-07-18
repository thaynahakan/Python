#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
from time import sleep

def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num:  O número a ser calculado.
    :return:  O valor do fatorial de um num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            sleep(0.3)
            print(c, end='')
            if c > 1:
                sleep(0.3)
                print(' x ', end='')
            else:
                sleep(0.3)
                print(' = ', end='')
        f *= c
    return f



print(fatorial(5, show=True))
