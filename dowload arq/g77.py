#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
#(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('caneta','papel','Violino','areia','teclado', 'batom')
print('=-' *30)
print(f' {"Programa das Vogais":^40}')
for letra in palavras:
    print(f'\n A palavra {letra}  tem as vogais', end = '')
    for p in letra:
        if p.lower() in 'aeiou':
            print(f'  {p}', end='')



print('=-' *30)

for c, v in enumerate(palavras):

    print(f' Na posição {c+1} encontrei a palavra {v}')