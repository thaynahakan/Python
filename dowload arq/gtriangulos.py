print('Analisador de triangulos!')

l1 = float(input('lado A:'))
l2 = float(input('lado B:'))
l3 = float(input('lado C:'))

if l1 < l2 + l3 and l2 < l1 + l3 and  l3 < l1 + l2:
    print('Pode formar um triangulo', end='')
if l1 == l2 == l3:
    print(' EQUILATERO')
elif l1 != l2 != l3 != l1:
    print(' ESCALENO')
elif l1 == l2 != l3 or l2 == l3 != l1:
    print(' ISOCELES')
else:
    print('Os segmentos acima não podem formar um Triangulo!')


