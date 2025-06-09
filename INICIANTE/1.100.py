numeros = [1, 2, 3, 4, 5, 6 ,7, 8]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
entrada = map(input().split())

a = entrada[0]
b = entrada[1]

lA = a[0]
numA = int(a[1])

lB = b[0]
numB = int(b[1])

c = numB - numA
if c < 0:
    c = numA-numB

colunas = c


linhas = 0

for i in range(len(letras)):
    l1, l2 = linhas
    if letras[i] == lA:
        l1 = i
    if letras[i] == lB:
        l2 = i

    l = l1-l2
    if l < 0:
        l = l2-l2

    linhas += l


resultado = 'Não consegui'

print(f'To get from {a} to {b} takes {resultado} knight moves.')