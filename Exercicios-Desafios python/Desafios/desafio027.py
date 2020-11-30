nome = input('Digite seu nome completo: ')
nome = nome.split()
print(f'O primeiro nome é {nome[0]}')
nome = nome[::-1]
print(f'O ultimo nome é {nome[0]}')
