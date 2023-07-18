
preco = float(input('Valor do Produto:'))

print('''Escolha a forma de Pagamento.
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')

forma = int(input("Escolha:"))

if forma == 1:
    total = preco - (preco * 10/100)
    print(total)
elif forma == 2:
    total = preco - (preco * 5/100)
    print(total)
elif forma == 3:
    parcela = preco/2
    print(f'O valor será de:{preco}, em duas parcelas de {parcela}R$')
elif forma == 4:
    totp = int(input('Quantas vezes?'))
    total = preco + (preco * 20 / 100)
    parcela = total / totp
    print(f' O valor total será {total} dividido em {totp}x de {parcela} R$')
    print(total)
else:
    print('Erro, opção Inválida')