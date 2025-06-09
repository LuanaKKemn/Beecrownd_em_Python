
def percentuando(num, total):
    return (num/total)*100

n = int(input())

dicCobaias = {}
for i in range(n):
    entrada = list(input().split())
    num = int(entrada[0])
    name = (entrada[1])
    if name not in dicCobaias:
        dicCobaias[name] = int(num)
    else:
        dicCobaias[name] += int(num)

total = sum(dicCobaias.values())
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {dicCobaias['C']}")
print(f"Total de ratos: {dicCobaias['R']}")
print(f"Total de sapos: {dicCobaias['S']}")
print(f"Percentual de coelhos: {percentuando(dicCobaias['C'], total):.2f} %")
print(f"Percentual de ratos: {percentuando(dicCobaias['R'], total):.2f} %")
print(f"Percentual de sapos: {percentuando(dicCobaias['S'], total):.2f} %")