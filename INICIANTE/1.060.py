
lista = []
positivos = 0
for i in range(6):
    num = float(input())
    lista.append(num)
    if num > 0:
        positivos += 1

lista.sort()

print(lista)


print(f'{positivos} valores positivos')

 