#crie um program para aprovar um emprestimo bancario para a compra de uma casa
# VALOR DA CASA, SALARIO E EM QUANTOS ANOS VAI PAGAR
#calcule valor mensal que não pode exceder 30% do salario

vcasa = float(input("Valor do imóvel:"))
s = float(input("Salário:"))
a = int(input("Anos para pagar:"))

meses = a * 12
parcela = vcasa / (a * 12)
minimo = s * 30 / 100
print(meses)

if parcela > minimo:
    print(f' O valor da parcela ficou de {parcela:.2f} R$, sendo superior a 30% do seu salário, emprestimo negado.')
else:
    print(f'Emprestimo concedido! O valor da parcela ficou de {parcela:.2f} R$')

