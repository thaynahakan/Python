#Exercício Python  075: Desenvolva um programa que leia quatro valores
# pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


    lista = []
    acumulador = 0
    nove = 0
    tres = 0
    pares = 0
    while acumulador < 4:
        valor = int(input('VALOR:'))
        acumulador += 1
        lista.append(valor)

        if valor == 9:
            nove += 1

        if valor == 3:
            tres = acumulador

        if valor % 2 == 0:
            pares += 1

    print(f' O valor 9 apareceu {nove} vezes')
    print(f' O valor 3 apareceu na posição {tres}')
    print(f' {pares} números pares.')
    print(lista)