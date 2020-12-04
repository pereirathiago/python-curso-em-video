'''
ANSI para cores
escape sequence

\033[style;text;backm
\033[0;33;44m
]] -> só para fechar nn precisara

STYLE
    0 None
    1 Bold
    4 Underline
    7 Negative
TEXT
    30 -> branco
    31 -> vermelho
    32 -> verde
    33 -> amarelo
    34 -> azul
    35 -> roxo
    36 -> magenta
    37 -> cinza
BACK
    40 -> branco
    41 -> vermelho
    42 -> verde
    43 -> amarelo
    44 -> azul
    45 -> roxo
    46 -> magenta
    47 -> cinza
'''

'''
TESTE \033[0;30;41m -> None;Branco;Vermelho]
TESTE \033[4;33;44m -> Underline;Amarelo;Azul]
TESTE \033[1;35;43m -> Bold;Roxo;Amarelo]
TESTE \033[30;42m -> Branco;Verde]
TESTE \033[m -> padrão]
TESTE \033[7;30m -> Inverter;Branca]
'''

# PRATICA

# print('\033[7;33;44mOla, Mundo!\033[m')
'''
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')'''
nome = 'thiago'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretobranco': '\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(
    cores['amarelo'], nome, cores['limpa']))

