linha = (input().split())
#   1 ≤ T ≤ 3000 - POPULAÇÃO
PA = int(linha[0])
PB = int(linha[1])
#   100 ≤ PA < 1000000, PA < PB ≤ 1000000
# Crescimento Populacional (em percentual)
G1 = float(linha[2])
G2 = float(linha[3])
#   0.1 ≤ G1 ≤ 10.0, 0.0 ≤ G2 ≤ 10.0, G2 < G1
# se o tempo for mais do que 100 anos o programa deve apresentar a mensagem: Mais de 1 seculo.
# POPULAÇAO
if (G2 == 0):
    G2 = 1
else:
    G2 = G2
populacaoPA = PA + (PA/G1*100)
populacaoPB = PB + (PB/G2*100)

PA = populacaoPA
PB = populacaoPB

#  CRESCIMENTO ANUAL

tempo = 1
tempo = tempo+1

if (PA + tempo*(PA/G1*100)) > (PB + tempo*(PB/G2*100)):
    print(tempo)


if populacaoPA > populacaoPB:
    print('quantos anos?')
else:
    print(populacaoPA, "<", populacaoPB)

tempo = 99
print(tempo)

if tempo > 100:
    print('Mais de 1 século.')
else:
    print(tempo, "anos.")
