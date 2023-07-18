# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo =str(input('Sexo[F/M]:')).upper().strip()[0]
while sexo not in 'MF':
    print('Inválido')
    sexo = str(input('Sexo[F/M]:')).upper().strip()

if sexo == 'M':
    print('Masculino')
if sexo == 'F':
    print('Feminino')

print(sexo)