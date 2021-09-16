num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua oção: '))
if opcao == 1:
    print('{} converteido para binario é igual a {}'.format(num, bin(opcao)[2:]))
elif opcao == 2:
    print('{} converteido para octal é igual a {}'.format(num, oct(opcao)[2:]))
elif opcao == 3:
    print('{} converteido para hexadecimal é igual a {}'.format(num, hex(opcao)[2:]))
else:
    print('Opção invalida. Tente novamente')
