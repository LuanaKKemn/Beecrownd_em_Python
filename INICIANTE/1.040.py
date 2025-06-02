linha = input().split()
n1 = float(linha[0])
n2 = float(linha[1])
n3 = float(linha[2])
n4 = float(linha[3])

media = (n1*2 + n2*3 + n3*4 + n4*1)/10

print('Media: %.1f' % media)
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5 and media < 7:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f' % n5)
    mediaFinal = (media + n5)/2
    if mediaFinal>=5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % mediaFinal)
