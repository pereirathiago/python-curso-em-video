s = int(input('Digite o valor do seu salario: '))

if s > 1250:
    ns = s * 0.1
    print(f'Seu novo salario é {ns + s:.2f}')
else:
    ns = s * 0.15
    print(f'Seu novo salario é {ns + s:.2f}')
