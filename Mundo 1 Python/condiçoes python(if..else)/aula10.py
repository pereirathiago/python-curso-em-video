'''
if carro.esquerda():
    bloco _V_
else carro.direita():
    bloco_F_
'''

'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('carro  novo')
else:
    print('carro velho')
print('--fim--')
'''

'''
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--fim--')
'''

# PRATICA

nome = str(input('Qual seu nome? '))
if nome == 'Thiago':
    print('Que nome lindo vc tem!')
else:
    print('Seu nome é tão normal!')
print('BOm dia. {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
'''
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
'''
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS!')
