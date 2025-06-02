
salario = float(input())

if salario <= 400.00:
    percent = 15
    salarioNovo = (salario * 0.15) + salario

elif salario <= 800.00:
    percent = 12
    salarioNovo = salario * 0.12 + salario

elif salario <= 1200.00:
    percent = 10
    salarioNovo = salario * 0.10 + salario

elif salario <= 2000.00:
    percent = 7
    salarioNovo = salario * 0.07 + salario

elif salario > 2000.00:
    percent = 4
    salarioNovo = salario * 0.04 + salario


reajuste = salarioNovo - salario

print(f'Novo salario: {salarioNovo:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percent} %')

