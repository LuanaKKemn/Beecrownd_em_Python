while True:
    entrada = list(map(int, input().split()))
    m = entrada[0]
    n = entrada[1]

    if m == 0 or n == 0:
        break

    lista = []
    for i in range(n,m+1):
        lista.append(i)
        print(i, end=' ')

    print(f'Sum={sum(lista)}')

