n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

if (media < 5):
    print(f'Média = {media} Reprovado')
elif (media >= 5 and media < 7):
    print(f'Média = {media} Recuperação')
else:
    print(f'Média = {media} Aprovado')
