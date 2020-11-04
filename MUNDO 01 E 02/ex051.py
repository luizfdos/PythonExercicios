# DESAFIO 051 - DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA.
# NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.
print('=' * 55)
print('{:^55}'.format('10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA'))
print('=' * 55)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(1, 11):
    print(termo, end=' → ')
    termo += razao
print('ACABOU')

'''METODO GUANABARA
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao:
for c in range(primeiro(c), decimo, razao):
    print('{} '.format(c), end= ' →')
'''
