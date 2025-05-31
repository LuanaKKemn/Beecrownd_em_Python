
import struct

Item = struct.Struct("i f")

def criaTabela(arq="tabela.bin"):

    precos = [
        (1, 4.0),  # Código 1, Cachorro Quente, Preço R$4.00
        (2, 4.5),  # Código 2, X-Salada, Preço R$4.50
        (3, 5.0),  # Código 3, X-Bacon, Preço R$5.00
        (4, 2.0),  # Código 4, Torrada Simples, Preço R$2.00
        (5, 1.5)  # Código 5, Refrigerante, Preço R$1.50
    ]

    with open(arq, "wb") as arquivo:
        for codigo, preco in precos:
            arquivo.write(Item.pack(codigo, preco))

def buscarPreco(arq, codigoBuscado):
    with open(arq, "rb") as arquivo:
        while True:
            dados = arquivo.read(Item.size)
            if not dados:
                break
            codigo, preco = Item.unpack(dados)
            if codigo == codigoBuscado:
                return preco
    return None


def calcularTotal():
    criaTabela()

    codigo, quantidade = map(int, input("Digite o código e a quantidade do item: ").split())

    preco = buscarPreco("tabela.bin", codigo)

    with open("saida.bin", 'wb') as saida:
        if preco is not None:
            total = preco * quantidade

            saida.write(struct.pack("f", total))
            print(f"Total calculado e escrito em 'saida.bin': R$ {total:.2f}")

calcularTotal()