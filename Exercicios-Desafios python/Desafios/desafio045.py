from random import randint
player = 0
print("Vamos jogar pedra, papel e tesoura")
while player > 4 or player < 1:
    player = int(input("Digite: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n ...: "))
comp = randint(1, 3)
if player == comp:
    print("Empate")
elif player == 1 and comp == 2:
    print("Eu venci, escolhi Papel")
elif player == 1 and comp == 3:
    print("Vc venceu, escolhi Tesoura")
elif player == 2 and comp == 1:
    print("Vc venceu, escolhi Pedra")
elif player == 2 and comp == 3:
    print("Eu venci, escolhi Tesoura")
elif player == 3 and comp == 1:
    print("Vc venceu, escolhi Papel")
elif player == 3 and comp == 2:
    print("Eu venci, escolhi Pedra")