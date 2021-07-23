peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2

if(imc < 18.5):
    print(f'Seu IMC é {imc:.2f} ABAIXO DO PESO')
elif(imc >= 18.5 and imc < 25):
    print(f'Seu IMC é {imc:.2f} PESO IDEAL')
elif(imc >= 25 and imc < 30):
    print(f'Seu IMC é {imc:.2f} SOBREPESO')
elif(imc >= 30 and imc < 40):
    print(f'Seu IMC é {imc:.2f} OBESIDADE')
else:
    print(f'Seu IMC é {imc:.2f} OBESIDADE MORBIDA')
