
num = int(input('Digite o número inteiro:'))
print('''Escolha uma Linguagem para conversão:
        [1] Binário
        [2] Octal
        [3] Hexadecimal''')

opcao = int(input('Digite a opção:'))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida')

