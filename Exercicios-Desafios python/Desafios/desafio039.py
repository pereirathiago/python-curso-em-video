import time
anoAtual = int(time.strftime('%Y', time.localtime()))
anoNasc = int(input('Digite o ano que você nasceu: '))

idade = anoAtual - anoNasc

if(idade == 18):
    print(f'Você tem {idade} anos. Chegou a hora de se alistar')
elif(idade > 18):
    print(f'Passou {idade - 18} anos da hora de se alistar')
elif(idade < 18):
    print(f'Ainda não é hora de se alistar. Falta {18 - idade} anos')
