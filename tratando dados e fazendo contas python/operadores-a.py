'''
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))  # com 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome))  # alinhado na direita
print('Prazer em te conhecer {:<20}!'.format(nome))  # alinhado na esquerda
print('Prazer em te conhecer {:^20}!'.format(nome))  # centralizado
print('Prazer em te conhecer {:=^20}!'.format(nome))  # centralizado com =
'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e \n a divisão é {:.3f}'.format(s, m, d), end='>>>')
# end não quebra linha
print('Divisão inteira {} e a potência {}'.format(di, e))
