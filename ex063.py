# DESAFIO 063 - ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER E MOSTRE
# NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI.
# EX: 0 → 1 → 1 → 2 → 3 → 5 → 8
print('=' * 50)
title = 'Sequência de Fibonacci'
print(f'{title:^50}')
print('=' * 50)
limite = int(input('Quantos termos você quer mostrar?: '))
anterior = 1
proximo = 0
print('~' * 50)
# for i in range(0, limite): exemplo com for ao invés de while
while limite > 0:
    print(proximo, end=' → ')
    proximo += anterior
    anterior = proximo - anterior
    limite -= 1
print('FIM')
print('~' * 50)

# primeira repetição
# usuario digita: 10 (limite recebe 10)
# Imprime 0
# proximo += anterior (proximo recebe 0 +1, ou seja, proximo = 1)
# anterior = proximo - anterior (anterior recebe 1 - 1, ou seja, anterior = 0)
# (limite recebe 10 - 1 = 9)

# segunda repetição
# imprime 1
# proximo += anterior (proximo recebe 1 + 0, ou seja, proximo = 1)
# anterior = proximo - anterior (anterior recebe 1 - 0, ou seja, anterior = 1)
# (limite = 9 - 1 = 8)

# terceira repetição
# imprime 1
# proximo += anterior (proximo recebe 1 + 1, ou seja, proximo = 2)
# anterior = proximo - anterior (anterior recebe 2 - 1, ou seja, anterior = 1)
# (limite = 8 - 1 limite = 7)

# quarta repetição
# imprime 2
