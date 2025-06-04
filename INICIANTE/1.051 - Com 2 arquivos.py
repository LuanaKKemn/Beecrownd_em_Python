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


with open("salario.txt", "r") as arq, open("saida.txt", "w") as saida:
    for linha in arq:
        #print(linha)
        salario = float(linha)

        if salario<2000:
            saida.write('Isento\n')

        elif salario <= 3000:
            imposto = porcent8(salario)
            saida.write(f'R$ {imposto:.2f}\n')

        elif salario <= 4500:
            imposto = porcent8(salario) + porcent18(salario)
            saida.write(f'R$ {imposto:.2f}\n')

        elif salario > 4500:
            imposto = porcent8(salario) + porcent18(salario) + porcent28(salario)
            saida.write(f'R$ {imposto:.2f}\n')
