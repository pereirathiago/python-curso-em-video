import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
conseno = math.cos(math.radians(an))
print('O ângulo de {} tem o COSCENO de {:.2f}'.format(an, conseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, tangente))
