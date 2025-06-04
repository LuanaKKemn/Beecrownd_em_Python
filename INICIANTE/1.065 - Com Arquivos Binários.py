import struct

Sequencia = struct.Struct("i i i i i")

def escreveBinario(arq, lista):
    with open(arq, 'wb') as entrada:
        entrada.write(Sequencia.pack(*lista))


def lerBinario(arq):
    with open(arq, "rb") as saida:
        dado = saida.read(Sequencia.size)
        info = list(Sequencia.unpack(dado))
        #print(info)
        return info


def contaPares(lista):
    pares = 0
    for item in lista:
        if item % 2 == 0:
            pares += 1
    return pares


def saidaBinaria(arq, pares):
    with open(arq, 'wb') as dados:
        dados.write(f'{pares} valores pares\n'.encode('utf-8'))


def printaSaidaBinaria(arq):
    with open(arq, 'rb') as dados:
        while True:
            binarios = dados.readline()

            if not binarios:
                break

            print(binarios.decode('utf-8').strip())


escreveBinario("entrada.bin", [8, -5, 6, -4, 12])

lista = lerBinario("entrada.bin")

pares = contaPares(lista)

saidaBinaria("saida.bin", pares)

print("Conteudo de 'saida.bin':")
printaSaidaBinaria("saida.bin")