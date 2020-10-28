print('====== DESAFIO 04 ======')

a = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Esta em maiúsculas? {a.isupper()}')
# print(f'Esta em minúsculas? {a.is()}')
# print(f'Esta capitalizada? {a.is()}')

