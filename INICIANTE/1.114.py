acertou = 0
senha = 2002

while acertou == 0:
    num = int(input())
    if num != senha:
        print("Senha Invalida")
    else:
        acertou += 1

print("Acesso Permitido")