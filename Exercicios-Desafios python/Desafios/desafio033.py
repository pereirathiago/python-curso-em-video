x = int(input('Digite um núemro: '))
y = int(input('Agora outro: '))
z = int(input('E outro: '))

if x > y and x > z:
    print(f'{x} é maior')
elif x < y and y > z:
    print(f'{y} é maior')
else:
    print(f'{z} é maior')

if x < y and x < z:
    print(f'{x} é mwnor')
elif x > y and y < z:
    print(f'{y} é menor')
else:
    print(f'{z} é menor')
