with open("seq.txt", "r") as numbers, open("saida.txt", "w") as saida:
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
            saida.write(f"{i} ")

        saida.write(f'Sum= {sum(lista)}\n')
