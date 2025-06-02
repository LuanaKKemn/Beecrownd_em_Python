a, b, c = map(float, input().split())

lados = sorted([a, b, c], reverse=True)
A, B, C = lados

if A < B + C:
    perimetro = A + B + C

    print(f"Perimetro = {perimetro}")

else:
    area = (A + B) * C / 2

    print(f"Area = {area}")
