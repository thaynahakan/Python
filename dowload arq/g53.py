# Desenvolva um programa que leia uma frase e diga se ela é um palindromo

frase = input('Digite a frase:').upper().strip()
palavras = frase.split()
junta = ''.join(palavras)
print(junta)
print(palavras)
print(frase)

if junta == junta [::-1]:
    print('palindromo')
else:
    print('Não é palindromo')
