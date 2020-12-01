d = int(input('Digite a distancia em km da viagem: '))
if d > 200:
    print(f'O valor será R${d * 0.45}')
else:
    print(f'O valor será R${d * 0.50}')
