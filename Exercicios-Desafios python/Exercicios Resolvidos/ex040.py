nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {.:1} e {.:1}, a média do aluno é {.:1}.'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO')
