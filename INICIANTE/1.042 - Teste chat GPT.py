import struct

Sequencia = struct.Struct("i i i")


def escreverBinario(arq, lista):
    with open(arq, "wb") as entrada:
        entrada.write(Sequencia.pack(lista[0], lista[1], lista[2]))


def lerBinario(arq):
    with open(arq, "rb") as texto:
        dados = texto.read(Sequencia.size)
        listar = list(Sequencia.unpack(dados))
        return listar


def escreverSaidaBinaria(arq, listas):
    with open(arq, 'wb') as saida:
        for lista in listas:
            ordenada = sorted(lista)

            # Escreve os números ordenados
            for num in ordenada:
                saida.write(struct.pack("i", num))

            # Escreve um "marcador" de quebra de linha
            saida.write(struct.pack("i", 0))

            # Escreve os números na ordem original
            for num in lista:
                saida.write(struct.pack("i", num))


def printarArquivoBinario(arq):
    with open(arq, 'rb') as dado:
        while True:
            info = dado.read(4)

            if not info:
                break

            valor = struct.unpack("i", info)[0]

            # Se for o "marcador" de nova linha, imprime uma linha em branco
            if valor == 0:
                print()
                continue

            print(valor)


# Exemplo de várias listas
listas_de_entrada = [
    [7, 21, -14],
    [10, 5, 3],
    [-1, 0, 2]
]

# Escreve os dados de entrada para arquivos binários (opcional)
for i, lista in enumerate(listas_de_entrada):
    escreverBinario(f"entrada_{i}.bin", lista)

# Lê os dados de entrada e escreve a saída no arquivo binário
listas_lidas = [lerBinario(f"entrada_{i}.bin") for i in range(len(listas_de_entrada))]
escreverSaidaBinaria("saida.bin", listas_lidas)

# Imprime o conteúdo do arquivo de saída
print("Conteudo de 'saida.bin':")
printarArquivoBinario("saida.bin")
