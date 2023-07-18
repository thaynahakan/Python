#Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
from datetime import datetime

pessoa = dict()
lista = list()
somaidade = 0
while True:
    pessoa.clear()
    pessoa["nome"]=str(input("Digite um Nome:"))

    while True:
        pessoa["sexo"]=str(input("Digite um sexo[MASC/FEM]:")).upper().strip()[0]
        if pessoa["sexo"] not in 'MF':
            print("ERRO! Digite apenas M de masculino ou F de feminino.")

        if pessoa["sexo"] in 'MF':
            break
    id = int(input("Digite o ano de nascimento:"))
    pessoa["idade"] = datetime.now().year - id
    somaidade += pessoa["idade"]
    lista.append(pessoa.copy())

    while True:
        cont = str(input("Quer continuar?")).upper().strip()[0]
        if cont not in 'SN':
            print("ERRO! Digite apenas sim ou não.")
        if cont in 'SN':
            break
    if cont in "N":
        break
media = somaidade / len(lista)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é de:{media:5.2f}')
print(f'A lista de mulheres é de:', end='')
for p in lista:
    if p["sexo"] == 'F':
        print(f"{p['nome']} ", end='')
print()
print(f'A lista com pessoas com idade acima da média, são elas:')
for i in lista:
    if i["idade"] > media:
        print('      ', end='')
        for k, v in i.items():
            print(f'{k} = {v} ;', end='')
        print()




