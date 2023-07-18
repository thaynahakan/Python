#Faça um programa que calcule a soma dos numeros multiplos de 3
# Que se encontre no intervalo entre 1,500

i = 0
acum = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        i =  i + 1
        acum = acum + c
    print(c, end=' ')

print(f' Existem {i} numeros multiplos de 3 nessa range e a soma deles é: {acum}')







