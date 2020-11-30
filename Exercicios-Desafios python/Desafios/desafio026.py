frase = input('Digite uma frase: ')

frase = frase.lower()
na = frase.count('a')
a1 = frase.find('a')
an = frase.rfind('a')

print(f'A letra "a" aparece {na} vezes')
print(f'A letra "a" aparece pela primeira vez em {a1}')
print(f'A letra "a" aparece pela ultima vez em {an}')
