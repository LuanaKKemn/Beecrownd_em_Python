vendedor = str(input())
salario = float(input())
vendas = float(input())
comissao = 0.15*(vendas)
total = salario+comissao
print(f'TOTAL = R$ {total:.2f}')