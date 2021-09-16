preco = float(input('Digite o preço: '))
formaPagamenteo = int(input(' 1 - Dinheiro \n 2 - À vista no cartão \n 3 - 2x no cartão \n 4 - 3x no cartão \n Digite a opção:  '))

if(formaPagamenteo == 1):
    novoValor = preco * 0.9
    print(f'O valor do produto fica {novoValor:.2f}')
elif(formaPagamenteo == 2):
    novoValor = preco * 0.95
    print(f'O valor do produto fica {novoValor:.2f}')
elif(formaPagamenteo == 3):
    print(f'O valor do produto fica {preco:.2f}')
elif(formaPagamenteo == 4):
    juro = preco * 0.2
    novoValor = preco + juro
    print(f'O valor do produto fica {novoValor:.2f}')
else:
    print(f'Digite uma forma de pagamento.')
