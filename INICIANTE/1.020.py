dias = int(input())

ano = dias//365
restoAno = dias % 365
mes = restoAno//30
restoMes = restoAno % 30
dia = restoMes//1

print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')