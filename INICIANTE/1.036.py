import math

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

delta = b*b-4*a*c

if delta < 0 or a==0:
    print('Impossivel calcular')
else:
    delta = b * b - 4 * a * c
    R1 = (-b+ math.sqrt(delta))/(2*a)
    R2 = (-b- math.sqrt(delta))/(2*a)

    print('R1 = %.5f' % R1)
    print('R2 = %.5f' % R2)