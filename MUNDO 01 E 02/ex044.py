# DESAFIO - 044 - ELABORA UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO,
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:
#   1- À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#   2- À VISTA NO CARTÃO: 5% DE DESCONTO
#   3- EM ATÉ 2x NO CARTÃO: PREÇO NORMAL
#   4- 3X OU MAIS NO CARTÃO: 20% DE JUROS
print('{:=^40}'.format(' LOJAS CHERRY '))
valor = float(input("Digite o valor do produto R$: "))
condicao = str(input(
    'Opções de pagamento:\n[ 1 ] À VISTA DINHEIRO/CHEQUE\n[ 2 ] DÉBITO\n[ 3 ] 2x CARTÃO\n[ 4 ] 3x OU MAIS NO CARTÃO\nEscolha a opção desejada: '))
if condicao == '1':
    print(f'R${valor:.2f} - R${valor * 0.1:.2f}(10%): Valor a ser pago R${valor - (valor * 0.1):.2f}')
elif condicao == '2':
    print(f'R${valor:.2f} - R${valor * 0.05:.2f}(5%)\nValor a ser pago R${valor - (valor * 0.05):.2f}')
elif condicao == '3':
    print(f'Sua compra será parcelada em 2x de R${valor / 2:.2f}')
elif condicao == '4':
    parcelas = int(input('Quantas parcelas? '))
    print(
        f'Sua compra será parcelada em {parcelas}x de R${(valor + (valor * 0.2)) / parcelas:.2f}\nR${valor:.2f} + {valor * 0.2:.2f}(20%) Valor a ser pago R${valor + (valor * 0.2):.2f}')
else:
    print('\033[31mOPÇÃO INVÁLIDA de pagamento!\033[0m')
