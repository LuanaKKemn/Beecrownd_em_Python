n = int(input())

for teste in range(0, n):
    entrada = input().split()
    pa = int(entrada[0])
    pb = int(entrada[1])
    g1 = float(entrada[2])/100
    g2 = float(entrada[3])/100
    anos = 0
    while True:
        pa += int(pa*g1)
        pb += int(pb*g2)
        anos += 1

        if pa > pb or anos > 100:
            break

    if anos <= 100:
        print(anos, 'anos.')
    else:
        print("Mais de 1 seculo.")