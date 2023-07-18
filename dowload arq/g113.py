#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print(f'\033[0:31mERRO! O usuário preferiu não informar dados .\033[m')
            return 0
        except (ValueError,TypeError):
            print(f'\033[0:31m Por favor, digite um valor inteiro.\033[m')
            continue
        else:
            return n
            break


def leia_float(msg):
    while True:
        try:
            h = str(input(msg)).replace(',','.')
            h.isnumeric()
            return float(h)
        except (ValueError,TypeError):
            print(f'\033[0:31mErro! Digite um valor que preste, deixe de palhaçada.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0:31m O usuário preferiu não informar um valor.\033[m')
            return 0
        else:
            return h


n = leia_int('Digite um numero inteiro: ')
h = leia_float('Digite um Número Real:')
print(f' Você digitou o valor {n} inteiro e {h} que é um número flutuante.')
