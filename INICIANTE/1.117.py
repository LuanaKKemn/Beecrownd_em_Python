


notas = []

for i in range(2):
    nota = float(input())
    while nota < 0 or nota > 10:
        print("nota invalida")
        nota = float(input())
    notas.append(nota)

media = (notas[0] + notas[1]) / 2

print(f"media = {media}")
