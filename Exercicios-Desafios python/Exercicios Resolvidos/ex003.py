n1 = int(input('\033[33mDigite um valor:\033[m '))
n2 = int(input('\033[35mDigite outro valor:\033[m '))
s = n1 + n2
print('A soma entre \033[33m{}\033[m e \033[35m{}\033[m é igual a \033[32m{}\033[m!'.
      format(n1, n2, s))
