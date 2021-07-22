primeiroValor = float(input('Digite o primeiro valor: '))
segundoValor = float(input('Digite o segundo valor: '))

if (primeiroValor > segundoValor):
    print('O primeiro valor é maior')
elif (primeiroValor < segundoValor):
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')