from typing import Counter

n = int(input())

lista = []
for i in range(n):
    entrada = int(input())
    lista.append(entrada)

dic = Counter(lista)

for num in sorted(dic):
    print(f'{num} aparece {dic[num]} vez(es)')