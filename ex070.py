# DESAFIO 070 - CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS.
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR. NO FINAL, MOSTRE:
#  A) QUAL É O TOTAL GASTO NA COMPRA.
#  B) QUANTOS PRODUTOS CUSTAM MAIS DE R$ 1000.
#  C) QUAL É O NOME DO PRODUTO MAIS BARATO
precomaisbarato = total = maisquemil = cont = 0
print(40 * '-')
print('            LOJA SUPERBARATAO')
print(40 * '-')
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    if cont == 1 or preco < precomaisbarato:
        precomaisbarato = preco
        nomemaisbarato = nome
    if preco > 1000:
        maisquemil += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}\n'
      f'Temos {maisquemil} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {nomemaisbarato} que custa R$ {precomaisbarato:.2f}')
