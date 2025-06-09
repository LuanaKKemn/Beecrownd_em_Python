maior = 0
posicao = 0

lista = []

for i in range(3):
    num = int(input())
    lista.append(num)

    if i == 0:
        maior = num
    else:
        if maior < num:
            maior = num
            posicao = i+1

lista.sort()
print(lista)

print(maior)
print(posicao)
