# DESAFIO 035 - ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
# O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELES VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EM-
# PRÉSTIMO SERÁ NEGADO.
valorcasa = float(input('Valor casa R$ '))
salario = float(input('Salário R$ '))
anos = int(input('Anos: '))
meses = anos * 12
vlrparcela = valorcasa / meses
porcsalario = vlrparcela * 100 / salario
print(f'Para pagar o imovél de R${valorcasa:.2f} em {anos} anos a prestação será de R${vlrparcela:.2f}:')
if porcsalario > 30:
    print(f'Infelizmente o empréstimo foi \033[4:31mNEGADO\033[0m!\nCom seu salário de R${salario:.2f} o valor máximo da parcela permitido seria de R${salario*.3:.2f}')
else:
    print('O empréstimo foi \033[4:32mAPROVADO\033[0m!')