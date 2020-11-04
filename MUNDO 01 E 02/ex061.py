# DESAFIO 060 - REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA,
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
print('=' * 55)
print('{:^55}'.format('10 TERMOS DE UMA PROGRESSÃO ARITIMÉTICA'))
print('=' * 55)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao  # também poderia ser feito com contador e diminuir o valor a cada repetição ao invés de
while termo <= decimo:
    print(termo, end=' → ')
    termo += razao
print('FIM')
'''
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 10
while decimo > 0:
    print(termo)
    termo += razao
    contador -= 1
'''
