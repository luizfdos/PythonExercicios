# DESAFIO 060 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.
'''Ex:
5! = 5x4x3x2x1=120
'''
multiplicação = 1
numero = int(input('Digite um numero para calcular seu Fatorial: '))
fat = numero
print(f'{numero} ! = ', end='')
while fat > 0:
    print(fat, end='')
    print(' x 'if fat > 1 else ' = ', end='')
    multiplicação *= fat
    fat -= 1
print(multiplicação)

'''
# COM FOR
numero = int(input('Digite um numero para calcular seu Fatorial: '))
fatorial = 1
numerostr = str(numero)
print(numerostr+'! = ', end='')
for i in range(numero, 1, -1):
    print(i, end=' x ')
    fatorial *= i
print(1, '= ',fatorial)'''

''' COM MÓDULO
from math import factorial
n int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''