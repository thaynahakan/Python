#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome:'))
ano = int(input('Ano de nascimento:'))
cadastro['idade'] = datetime.now().year - ano
cadastro['carteira'] = int(input('CTPS:'))

if cadastro['carteira'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação:'))
    cadastro['salario'] = float(input('Salário:'))
    cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)


for n,v in cadastro.items():
    print(f'  -  {n}: {v}')