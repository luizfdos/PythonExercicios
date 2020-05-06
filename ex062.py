# DESAFIO 060 - REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA,
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
# MELHORE O DESAFIO 061, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR
# MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUADO ELE DISSER QUE QUER MOSTRAR 0 TERMOS
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
termos = 10
quantidade = 0
while termos > 0:
    contador = termos
    while contador > 0:
        print(termo, end=' > ')
        termo += razao
        contador -= 1
    quantidade += termos
    print('PAUSA')
    termos = int(input('Deseja exibir mais quantos termos?[Digite 0 para sair] '))
print('FIM')
print(f'Foram exibidos {quantidade}')
