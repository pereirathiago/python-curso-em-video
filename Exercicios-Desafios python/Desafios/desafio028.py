from random import randint
n = randint(1, 5)
print('Pensei em um número')
nu = int(input('Qual número vc acha que é?'))
print('PARABENS!' if nu == n else 'O PC VENCEU!')
