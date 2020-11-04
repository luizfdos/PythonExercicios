# DESAFIO 052 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU
# NÃO UM NÚMERO PRIMO
numero = int(input('Digite número: '))
divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(i, end=' ')
print(f'\n\033[mO número {numero} foi divisível {divisores} vezes')
if divisores == 2:
    print(f'E por isso ele É PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')
