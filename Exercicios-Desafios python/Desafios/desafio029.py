v = int(input('Digite a velocidade do veiculo: '))
if v > 80:
    print('Você passou do limite de velocidade!')
    print(f'Multa de R${(v - 80) * 7:.2f}')
