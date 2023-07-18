# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
i = 0

while True:
    n = int(input('Você quer a Tabuada de qual valor?'))
    if n < 0:
        print('Programa encerado, gOOD By3')
        break


    print(f'Tabuada de {n}')
    for i in range(1,11):
        print(f'{n} X {i} = {n * i}')
        i = i + 1
    print(f'-=' * 12)


print(f'-='* 12)
