
while True:
    n=0
    notas = []
    while n < 2:
        nota = float(input())
        if nota > 10 or nota < 0:
            print('nota invalida')
        else:
            notas.append(nota)
            n+=1

    media = (sum(notas))/2
    print(f'media={media:.2f}')
    print('novo calculo (1-sim 2-nao)')
    entrada = int(input())

    if entrada != 1:
        break
