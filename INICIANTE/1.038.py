
lanche = list(map(int, input().split()))

dicionario = {1:4, 2:4.5, 3:5, 4:2, 5:1.5}

total =  dicionario[lanche[0]] * lanche[1]

print(f'Total: R$ {total:.2f}')