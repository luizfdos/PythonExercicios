# DESAFIO 074 - CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA
# TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O 
# MAIOR VALOR QUE ESTÃO NA TUPLA

import random

numbers = (random.sample(range(1, 10), 5))
print('Os números sorteados foram: ', end='')
for number in numbers: 
  print(number, end=' ')

print(f'\nO maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')
