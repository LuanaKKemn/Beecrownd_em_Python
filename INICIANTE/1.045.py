a, b, c = map(float, input().split())

lados = sorted([a, b, c], reverse=True)
A, B, C = lados

if A >= B + C:
    print("NAO FORMA TRIANGULO")

else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")

    elif A ** 2 > (B ** 2 + C ** 2):
        print("TRIANGULO OBTUSANGULO")

    elif A ** 2 < (B ** 2 + C ** 2):
        print("TRIANGULO ACUTANGULO")


    if A == B and A == C:
        print("TRIANGULO EQUILATERO")

    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
