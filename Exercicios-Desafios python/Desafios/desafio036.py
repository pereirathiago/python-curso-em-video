# Recebendo valores
valorCasa = str(input('Digite o valor da casa: ')).strip()
valorCasa = float(valorCasa)
sal = str(input('Seu salario: ')).strip()
sal = float(sal)
anos = str(input('Quando anos deseja pagar: ')).strip()
anos = float(anos)

# calculando parcelas
valorParcela = valorCasa / anos

# If para verificação
sal30 = sal * 0.3  # 30% do salario
if sal30 >= valorParcela:
    print('Você pode financiar essa casa')
else:
    print('Você não pode financiar essa casa')
