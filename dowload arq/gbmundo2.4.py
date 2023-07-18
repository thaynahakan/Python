from datetime import date

sexo = int(input('''Sexo
    [1] Feminino
    [2] Masculino:
    Digite: '''))

if sexo == 1:
    print(" Mulheres não tem alistamento obrigatório.")

atual = date.today().year
nascimento = int(input('Digite o ano de nascimento:'))
anos = atual - nascimento


print(f' Quem nasceu em {nascimento} tem {anos} anos, em {atual}.')

if anos == 18:
    print(f' Esse ano você precisa se alistar, você vai completar {anos} anos!')
elif anos < 18:
    saldo = 18 - anos
    falta = atual + saldo
    print(f' Faltam {saldo} anos pra você se alistar.')
    print(f' Seu alistamento será em {falta}')
elif anos > 18:
    saldo = anos - 18
    falta = atual - saldo
    print(f' Você deveria ter se alistado há {saldo} anos.')
    print(f' Seu alistamento foi em {falta}.')