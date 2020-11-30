c = 0
n = int(input('Digite um número entre 0 e 9999: '))
while n > 9999 or n < 0:
    n = int(input('Digite um número entre 0 e 9999: '))

n = str(n)
n += '000'
print(f'Unidades: {n[0]}')
print(f'Dezenas: {n[1]}')
print(f'Centenas: {n[2]}')
print(f'Milhares: {n[3]}')
