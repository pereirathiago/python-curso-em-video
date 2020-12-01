salario = float(input('Qual é o slaraio do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhava R${:.2f}'.format(salario, novo))
