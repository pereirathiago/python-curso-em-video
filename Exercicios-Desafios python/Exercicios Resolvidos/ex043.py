peso = float(input('Digite o seu peso (Kg) '))
altura = float(input('Digite sua altura (m) '))
imc = peso / (altura **2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Você, está na faixa do seu peso normal')
elif 25 <= imc < 30:
    print('Você, está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você, está em OBSIDADE')
elif imc >= 40:
    print('Você, está em OBSIDADE MORBIDA')
