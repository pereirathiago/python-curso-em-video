x1 = int(input('Informe um dos lados: '))
x2 = int(input('Informe outro lado: '))
x3 = int(input('Informe mais um lado: '))

if (x1 + x2) > x3:
    if (x1 + x3) > x2:
        if(x2 + x3) > x1:
            if (x1 == x2 == x3):
                print('Será formado um triangulo equilatero')
            elif (x1 == x2 or x1 == x3 or x2 == x3):
                print('Será formado um triangulo isósceles')
            elif(x1 != x2 != x3):
                print('Será formado um triangulo escaleno')
        else:
            print('Não consigo um triangulo')
    else:
        print('Não consigo um triangulo')
else:
    print('Não consigo um triangulo')
