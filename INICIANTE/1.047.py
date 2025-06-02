a, b, c, d = map(int, input().split())

# a:b - c:d
inicio_Min = a * 60 + b
final_Min = c * 60 + d

if inicio_Min >= final_Min:
    final_Min += 24*60

duracaoTotal = final_Min - inicio_Min

horas = duracaoTotal // 60
minutos = duracaoTotal % 60


print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")