print('====== DESAFIO 08 ======')

n = float(input('Digite o valor em metros: '))

km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('''O medida de {}m corresponde a
{}km
{}hm
{}dam
{}dm
{}cm
{}mm'''.format(n, km, hm, dam, dm, cm, mm))
