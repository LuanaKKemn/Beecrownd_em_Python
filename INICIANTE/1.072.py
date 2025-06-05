n = int(input())

valores = []
inn = 0
out = 0
for i in range(n):
    valor = int(input())
    valores.append(valor)
    if 10 <= valor <= 20:
        inn+=1
    else:
        out +=1


print(f"{inn} in\n{out} out")
