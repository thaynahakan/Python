print('IMC')

peso = float(input('peso:'))
altura = float(input('altura:'))


imc = peso/(altura**2)
print(f'IMC:{imc:.1f}')

if imc < 18.5:
    print('Abaixo do Peso')
elif imc > 18.5 and imc < 25:
    print('Peso ideal')
elif imc > 25 and imc < 30:
    print('Sobrepeso')
elif imc > 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')