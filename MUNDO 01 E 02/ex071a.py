# DESAFIO 071 - CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO.
# NO INICIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO(NÚMERO INTEIRO) E O
# PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES.
# OBS: CONSIDERANDO QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1.
total1 = total10 = total20 = total50 = 0
print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
valor = int(input("Que valor você quer sacar? R$ "))
while  True:
    total50 = valor // 50
    restante = valor - (total50*50)
    if restante == 0:
        break
    else: 
        total20 = restante // 20
        restante -= (total20 * 20)
    if restante == 0:
        break
    else: 
        total10 = restante // 10 
        restante -=(total10*10)
    if restante == 0:
        break
    else:
        total1 = restante // 1
        break
print('=' * 40)
if total50 != 0:
    print(f'Total de {total50} ', end='')
    print('cédulas de R$50' if total50 > 1 else 'cédula de R$50')
if total20 != 0:
    print(f'Total de {total20} ', end='')
    print('cédulas de R$20' if total20 > 1 else 'cédula de R$20')
if total10 != 0:
    print(f'Total de {total10} ', end='')
    print('cédulas de R$10' if total10 > 1 else 'cédula de R$10')
if total1 != 0:
    print(f'Total de {total1} ', end='')
    print('cédulas de R$1' if total1 > 1 else 'cédula de R$1')
print('=' * 40)

