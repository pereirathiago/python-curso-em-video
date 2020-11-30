frase = 'Curso em vídeo Python'
# cada caracter consome um microespaço dentro do espaço
# 'frase' tem 21 micro-espaços, 0,1,2,3, ... , 20

# FATIAMENTO

frase[9]  # a letra 9 é V
frase[9:13]  # vai pegar do 9 até o 13, Vide
frase[9:21]  # vai pegar do 9 ao 21, sem contar o 21(nn existe)
frase[9:21:2]  # vai do 9 ao 21 pulando 2 em 2, VdoPto
frase[:5]  # == frase[0:5]
frase[15:]  # == frase[15:final]
frase[9::3]  # == frase[9:final:3]

# ANALISE

len(frase)  # comprimento
frase.count('o')  # conte quantas vezes aparece o 'o'
frase.count('o', 0, 13)  # conte quantas vezes aparece 'o' do 0 ao 13 -> 1 'o'
frase.find('deo')  # onde está o deo -> 11
frase.find('Android')  # retorna -1, nn existe

'Curso' in frase  # True ou False

#  Transformação

frase.replace('Python', 'Android')  # substitui python por Android
frase.upper()  # coloca tudo em maiusculo
frase.lower()  # coloca tudo em minúsculas
frase.capitalize()  # tudo para minúsculo menos a 1°
frase.title()  # Todas As Primeiras Letras Para  Maiusculas

frase = '   Aprenda Python  '
frase.strip()  # Apaga espaços inuteis inicio e fim
frase.rstrip()  # Apaga só da direita
frase.lstrip()  # Apaga só da esquerda

# Divisão

frase.split()  # separa nos espaços e gera uma lista
# ['Curso', 'em', 'Video', 'Python']

# Junção

'-'.join(frase)  # Junta a lista com um separador -
# Curso-em-Video-Python

# Pratica

frase = '   Curso em Video Python   '
# print(frase[3])
# print(frase[3:13])
# print(frase[:15])
# print(frase[1:15:2])
# print(frase[::2])

# print(frase.count('o'))
# print(len(frase.strip()))

# print(frase.replace('Python', 'Android'))
# print('Curso' in frase)
# print(frase.find('Curso'))
print(frase.split())
