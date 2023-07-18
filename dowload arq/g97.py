#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:

def linhas(txt):
    print('~'*len(txt))
    print(txt)
    print('~'*len(txt))


txt = str(input('Digite o texto:'))
linhas(txt)