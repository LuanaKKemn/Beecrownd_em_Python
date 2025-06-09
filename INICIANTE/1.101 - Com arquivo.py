with open("seq.txt", "r") as numbers:
    for linha in numbers:
        entrada = linha.split()
        m = int(entrada[0])
        n = int(entrada[1])

        if m == 0 or n == 0:
            break

        start = min(m, n)
        end = max(m,n)

        lista = []
        for i in range(n,m+1):
            lista.append(i)
            print(i, end=' ')

        print(f'Sum= {sum(lista)}')



