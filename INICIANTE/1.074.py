n = int(input())

tipos = {
    0 : "NULL",
    1 : "EVEN",
    2 : "ODD",
    3 : "POSITIVE",
    4 : "NEGATIVE",

}
for i in range(n):
    valor = int(input())

    if valor == 0:
        print(tipos[0])

    elif valor % 2 == 0:
        if valor > 0:
            print(tipos[1], tipos[3])
        else:
            print(tipos[1], tipos[4])

    else:
        if valor > 0:
            print(tipos[2], tipos[3])
        else:
            print(tipos[2], tipos[4])
