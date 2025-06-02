

a, b, c = map(int, input().split())

valores = [a, b, c]

if a <= b:
    if a < c:
        print(a)
        if b < c:
            print(b)
            print(c)
        else:
            print(c)
            print(b)
    else: # a > c:
        print(c)
        print(a)
        print(b)

elif b < a:
    if b < c:
        print(b)
        if a < c:
            print(a)
            print(c)
        else:
            print(c)
            print(a)
    else:
        print(c)
        print(b)
        print(a)



print()
print(a)
print(b)
print(c)
