def fibonacci (n, calls, memo):

    calls[0] += 1

    if n in memo:
        return memo[n]

    if n < 2:
        return n

    result = fibonacci(n-1, calls, memo) + fibonacci(n-2, calls, memo)
    memo[n] = result
    return result

num = int(input())

for i in range(num):
    f = int(input())
    calls = [0]
    memo = {}

    resultado = fibonacci(f, calls, memo)
    print(f"fib({f}) = {calls[0]} calls = {resultado}")