
def contarDiamantes(texto):
    pilha = []
    diamantes = 0

    for char in texto:
        if char == '<':
            pilha.append(char)
        elif char == '>' and pilha:
            pilha.pop()
            diamantes += 1
    return diamantes


n = int(input())

for i in range(n):
    entrada = input()



    print(contarDiamantes(entrada))