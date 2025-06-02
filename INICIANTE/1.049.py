ossos = input()

if ossos == 'vertebrado':
    familia = input()

    if familia == 'ave':
        tipo = input()

        if tipo == 'carnivoro':
            print("aguia")
        else:
            print("pomba")

    else:
        tipo = input()

        if tipo == 'onivoro':
            print("homem")
        else:
            print("vaca")


else:
    familia = input()

    if familia == 'inseto':
        tipo = input()

        if tipo == 'hematofago':
            print("pulga")
        else:
            print("lagarta")

    else:
        tipo = input()

        if tipo == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")