
valores = []

positivos = 0
total = 0.0

for i in range(6):
    valor = float(input())
    valores.append(valor)
    if valores[i] > 0:
        positivos += 1
        total += valor


print(f"{positivos} valores positivos")

if positivos > 0:
    media = total / positivos
    print(f"{media:.1f}")