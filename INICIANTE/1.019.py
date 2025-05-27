N=int(input())
horas=N//3600
RestoHoras=N%3600

minutos=RestoHoras//60
RestoMinutos=RestoHoras%60

segundos=RestoMinutos//1

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")