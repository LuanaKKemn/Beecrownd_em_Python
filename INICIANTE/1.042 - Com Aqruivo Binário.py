import struct

## CARREGAR VARIAS LISTAS PODE SER COMPLEXO PRA MIM AGORA ##

Sequencia = struct.Struct("i i i")

def escreverBinario(arq, lista):
    with open(arq, "wb") as entrada:
        entrada.write(Sequencia.pack(lista[0], lista[1], lista[2]))

def lerBinario(arq):
    with open(arq, "rb") as texto:
        dados = texto.read(Sequencia.size)
        listar = list(Sequencia.unpack(dados))
        #printarEOrdenar(listar)
        return listar

## Função auxiliar para testes ##
def printarEOrdenar(lista):
    ordenada = sorted(lista)
    for j in ordenada:
        print(j)
    print()
    for i in lista:
        print(i)

def escreverSaidaBinaria(arq, lista):
    ordenada = sorted(lista)

    with open(arq, 'wb') as saida:
        for num in ordenada:
            saida.write(struct.pack("i", num))

        saida.write(struct.pack("i", 0))
        ## Usa o 0 como marcados ##

        for num in lista:
            saida.write(struct.pack('i', num))


def printarArquivoBinario(arq):
    with open(arq, 'rb') as dado:
        while True:
            info = dado.read(4)

            if not info:
                break

            valor = struct.unpack('i', info)[0]

            if valor == 0:
                print()
                continue

            print(valor)


escreverBinario("entrada.bin", [7,21,-14])

lista = lerBinario("entrada.bin")

escreverSaidaBinaria("saida.bin", lista)

print("Conteudo de 'saida.bin':")
printarArquivoBinario("saida.bin")