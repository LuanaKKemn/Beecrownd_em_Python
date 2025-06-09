def percentuando(num, total):
    return (num/total)*100

dicCobaias = {}
cont = 0
with open("experiencias.txt", 'r') as arq:
    for linha in arq:
        if cont == 0:
            n = int(linha)
            cont += 1
        else:
            lista = linha.split()
            num = int(lista[0])
            name = (lista[1])
            if name not in dicCobaias:
                dicCobaias[name] = int(num)
            else:
                dicCobaias[name] += int(num)


total = sum(dicCobaias.values())

with open("saida.txt", "w") as saida:
    saida.write(f"Total: {total} cobaias\n")
    saida.write(f"Total de coelhos: {dicCobaias['C']}\n")
    saida.write(f"Total de ratos: {dicCobaias['R']}\n")
    saida.write(f"Total de sapos: {dicCobaias['S']}\n")
    saida.write(f"Percentual de coelhos: {percentuando(dicCobaias['C'], total):.2f} %\n")
    saida.write(f"Percentual de ratos: {percentuando(dicCobaias['R'], total):.2f} %\n")
    saida.write(f"Percentual de sapos: {percentuando(dicCobaias['S'], total):.2f} %")