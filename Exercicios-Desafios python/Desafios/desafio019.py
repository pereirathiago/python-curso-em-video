import random

alunos = input('Digite os alunos separados por ; ').split(";")
escolhido = random.choice(alunos)
print(f'O aluno escolhido foi {escolhido}')
