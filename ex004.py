# DESAFIO 004 - Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
# e todas as informações possíveis sobre ele
v = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(v)))
print('Só tem espaços? {}'.format(v.isspace()))
print('É número? {}'.format(v.isnumeric()))
print('É alfabético? {}'.format(v.isalpha()))
print('É alfanumérico? {}'.format(v.isalnum()))
print('Está em maiúsculas? {}'.format(v.isupper()))
print('Está em minúsculas? {}'.format(v.islower()))
print('Está capitalizada? {}'.format(v.istitle()))
print('É o melhor casal? True')
