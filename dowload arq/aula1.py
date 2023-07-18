# Projeto 1 - Prova
#Crie um código "prova.py" que irá aplicar uma 'prova' matemática.
## Parte 1
#Nesse código, deverão ser feitas 3 perguntas matemáticas.
#> as perguntas podem ser no estilo "Quanto é 3 + 5?".
#Para cada pergunta, deverá ser inputado a resposta.
#No final, deve ser impresso o gabarito correto das perguntas juntamente com a informação de quantas perguntas foram acertadas.
#> ATENÇÃO 45 é diferente de "45"!
import random

def prova_py(respost):
    print('-'*40)
    print('\033[1;31mProva Py de Matemática\033[m'.center(40))
    print('-' *40)

    prova = [('Quanto é: 12 + 4?','16'),('Quanto é 17 + 15?','32'),('Quanto é 96 + 45?','141'),
               ('Quanto é 5 - 44?','-39'),('Quanto é 76 - 67?','9'),('Quanto é 81 - 14?','67')]

    random.shuffle(prova)
    perguntas_sorteadas = random.sample(prova, 3)
    respostacerta = 0

    print("Responda as seguintes perguntas:")
    print('-' *40)

    for i,pergunta in enumerate(perguntas_sorteadas):
        print(f'Questão número {i+1}- {pergunta[0]}')
        resposta = str(input('Digite a resposta:')).strip()
        print('-'*40)
        print(f' {i+1}- Você respondeu:{resposta}.')
        if resposta == pergunta[1]:
            print('\033[1;36mResposta Correta\033[m')
            respostacerta += 1
            print('-' * 40)
        else:
            print(f'\033[1;31mERRADO! A resposta certa é {pergunta[1]}\033[m')
            print('-' * 40)
        i += 1
    print(f'\033[1;35m Você acertou {respostacerta} questões.\033[m')
    print(f' O gabarito das questões impresso é:')
    print(perguntas_sorteadas)

    if respostacerta == 2:
        print(f'\033[1;36mAprovado!\033[m')
    elif respostacerta > 2:
        print(f'\033[1;36mVocê teve excelência na sua nota, Parabéns!\033[m')
    else:
        print('\033[1;31mReprovado! Que demérito...\033[m')








prova_py(1)











