# DESAFIO 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6.
from math import floor
numero = float(input("Digite um número real: "))
print(f"O número {numero} tem a porção inteira {floor(numero)}.")

'''from math import trunc
numero = float(input("Digite um número real: "))
print(f"O número {numero} tem a porção inteira {trunc(numero)}.")'''
'''numero = float(input('Digite um valor: '))
print(f"O número {numero} tem a porção inteira {(numero:.0f)}.")'''

'''numero = float(input('Digite um valor: '))
print(f"O número {numero} tem a porção inteira {int=(numero)}.")'''

