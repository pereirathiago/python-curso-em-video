print('{:=^40}'.format(' Centralizado 40 espaços '))
preco = float(input('PReço das compras: R$ '))
print('''Formas de pagamento
[ 1 ] à vista em dinheito/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas'))
    parcela = total / total
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else: 
    total = 0 
    print('Opção invalida de pagamento')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'. format(preco, total))
