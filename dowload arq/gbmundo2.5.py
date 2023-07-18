from datetime import date

ano = int(input('Digite o ano de nascimento:'))
anos = date.today().year
idade = anos - ano
mirim = 9
infantil = 14
junior = 19
senior = 20

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade  <= 19:
    print('Junior')
elif idade > 19:
    print('Senior')
else:
    print('Master')