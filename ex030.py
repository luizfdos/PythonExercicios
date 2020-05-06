# DESAFIO - 030 - PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É ÍMPAR OU PAR.
from termcolor import colored
title = "ÍMPAR OR PAR"
print(colored(f'{title:=^51}', 'blue'))
numero = int(input('Digite o número que deseja saber se é ÍMPAR ou PAR: ').strip()) # verify if a interger is even or odd
if numero % 2 == 0:
    print(f'O número {numero} é:', colored('PAR', 'blue'))
else:
    print(f'O numéro {numero} é:', colored('ÍMPAR', 'blue'))