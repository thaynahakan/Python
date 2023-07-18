#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []

exp = str(input(' Digite a expresão:'))

for c in exp:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('Sua expressão está errada')
else:
    print('Sua expressão estava correta.')
