import time
anoAtual = int(time.strftime('%Y', time.localtime()))
anoNasc = int(input('Digite o ano que você nasceu: '))

idade = anoAtual - anoNasc

if(idade <= 9):
    print('Categoria Mirim')
elif(idade <= 14):
    print('Categoria Infantil')
elif(idade <= 19):
    print('Categoria Junior')
elif(idade == 20):
    print('Categoria Sênior')
else:
    print('Categoria Master')
    