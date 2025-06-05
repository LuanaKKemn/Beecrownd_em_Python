import struct

def preencheBinario(arq, n):
    with open(arq, 'wb') as entrada:
        entrada.write(struct.pack('i', n))

def lerBinario(arq):
    with open(arq, 'rb') as leitura:
        dado = leitura.read(4)
        n = struct.unpack('i', dado)[0]
        return n

def tabuadaBinaria(arq, n):
    with open(arq, 'wb') as saida:
        for i in range(1, 11):
            linha = f'{i} x {n} = {i*n}\n'
            saida.write(linha.encode('utf-8'))

def printaSaidaBinaria(arq):
    print(f"Conteúdo de '{arq}':")
    with open(arq, 'rb') as saida:
        while True:
            dado = saida.readline()

            if not dado:
                break

            print(dado.decode('utf-8').strip())


preencheBinario('entrada.bin', 140)

n = lerBinario('entrada.bin')

tabuadaBinaria('saida.bin', n)

printaSaidaBinaria('saida.bin')