#Exercício Python 062: Melhore o DESAFIO 061,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('       Gerador de PA')
print('=-'*15)
pa = int(input('Digite o primeiro numero da PA:'))
razao = int(input('Digite a PA que deseja:'))
contador = 1
termo =  pa
amais = 10
total = 0

while amais != 0:
    total += amais
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1

    print('PAUSA')
    amais = int(input('QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS?'))
print(f'O total de termos exibidos foram {total}')
print('Fim <3')

