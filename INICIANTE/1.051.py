def porcent8(salario):

    if salario>3000:
        salario = 3000

    calculo = salario - 2000

    return calculo*0.08

def porcent18(salario):

    if salario>4500:
        salario = 4500

    calculo = salario - 3000

    return calculo*0.18


def porcent28(salario):

    calculo = salario - 4500

    return calculo*0.28


salario = float(input())

if salario<2000:
    print('Isento')
elif salario <= 3000:
    imposto = porcent8(salario)
    print(f'R$ {imposto:.2f}')
elif salario <= 4500:
    imposto = porcent8(salario) + porcent18(salario)
    print(f'R$ {imposto:.2f}')
elif salario > 4500:
    imposto = porcent8(salario) + porcent18(salario) + porcent28(salario)
    print(f'R$ {imposto:.2f}')