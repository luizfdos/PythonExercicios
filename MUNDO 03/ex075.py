# DESAFIO 075 -  DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO E GUARDE-OS 
# EM UMA TUPLA. NO FINAL, MOSTRE:
# A) QUANTAS VEZES APARECEU O VALOR 9
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
# C) QUAIS FORAM OS NÚMEROS PARES.

numbers = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
evens = 0
print(f'Você digitou os valores {numbers}')
if 9 in numbers:
  print(f'O valor 9 apareceu {numbers.count(9)} vezes')  
else:
   print('O número 9 não foi digitado nenhuma vez.')

if 3 in numbers:
  print(f'O valor 3 apareceu na {numbers.index(3)+1}ª posição')  
else:
  print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end='')
for number in numbers: 
  if number % 2 == 0:
    evens += 1
    print(number, end=' ')
if evens == 0:
  print("Nenhum")
