#Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante 'a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0:31mERRO! Digite um valor válido.\033[m')
        if ok:
            break
    return valor


n = leia_int('Digite um numero: ')
print(f' Você digitou o valor {n}.')