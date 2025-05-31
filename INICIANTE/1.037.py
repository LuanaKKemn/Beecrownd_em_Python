entrada = float(input())

#([0,25], (25,50], (50,75], (75,100])

if 0 <= entrada <= 25:
    print('Intervalo [0,25]')
elif 25 < entrada <= 50:
    print('Intervalo (25,50]')
elif 50 < entrada <= 75:
    print('Intervalo (50,75]')
elif 75 < entrada <=100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

