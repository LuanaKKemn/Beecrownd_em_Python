def fibonnati(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibonnati(n-1) + fibonnati(n-2)


def imprimirfib(n):
    resultado = []

    for i in range(n):
        resultado.append(fibonnati(i))
    print(" ".join(map(str, resultado)))

n = int(input())

fibo = [0, 1]
for i in range(2, n):
    calc = fibo[i-1] + fibo[i-2]
    fibo.append(calc)

#print(" ".join(map(str, fibo)))

imprimirfib(n)