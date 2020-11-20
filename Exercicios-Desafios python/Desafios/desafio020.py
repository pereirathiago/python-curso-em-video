import random

alunos = input('Digite os alunos separados por ; ').split(";")
random.shuffle(alunos)
print(f'A ordem de apresentação será: \n{alunos}')
