numConv = conv = 0

while(conv != 4):
    decimal = int(input('Digite o número decimal: '))
    print('''
1 - Converter para binário
2 - Converter para hexadecimal
3 - Converter para octal
4 - Sair
    ''')
    conv = int(input('Escolha uma opção: '))

    if(conv == 1):
        numConv = format(decimal, "b")
        print(f'O número {decimal} em binário é {numConv}')
    elif(conv == 2):
        numConv = format(decimal, "x")
        print(f'O número {decimal} em hexadecimal é {numConv}')
    elif(conv == 3):
        numConv = format(decimal, "o")
        print(f'O número {decimal} em octal é {numConv}')
