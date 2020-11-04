# DESAFIO 059 - CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
'''[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA'''
menu = 0
for i in range(1, 3):
    if i == 1:
        n1 = int(input(f'Digite o {i}º número inteiro: '))
    else:
        n2 = int(input(f'Digite o {i}º número inteiro: '))
while menu != 5:
    menu = int(input(
        f'Escolha o que deve ser feito com os numéros {n1} e {n2}\n  [1]SOMAR\n  [2]MULTIPLICAR'
        '\n  [3]MAIOR\n  [4]NOVOS NÚMEROS\n  [5]SAIR DO PROGRAMA\nQual é a sua escolha: '))
    if menu == 1:  # SOMA
        print('=' * 60)
        print(f' {n1} + {n2} = {n1 + n2}')
        print('=' * 60)
    elif menu == 2:  # MULTIPLICA
        print('=' * 60)
        print(f' {n1} x {n2} = {n1 * n2}')
        print('=' * 60)
    elif menu == 3:  # MAIOR
        print('=' * 60)
        if n1 > n2:
            print(f' Entre {n1} e {n2} o maior é {n1}.')
            print('=' * 60)
        elif n2 > n1:
            print(f' Entre {n1} e {n2} o maior é {n2}.')
            print('=' * 60)
        else:
            print(f' Os dois são iguais')
            print('=' * 60)
    elif menu == 4:
        print('=' * 60)
        n1 = int(input(' Digite o primeiro número inteiro: '))
        n2 = int(input(' Digite o primeiro número inteiro: '))
        print('=' * 60)
    elif menu == 5:
        print('Até mais!')
    else:
        print('OPÇÃO INVÁLIDA!')
        print('=' * 60)
