# DESAFIO 064 - CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR
# E O MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU
# NÃO CONTINUAR A DIGITAR VALORES.
continuar = 'S'
quantidade = soma = media = maior = menor = 0
while continuar not in 'Nn':
    numero = int(input('Digite um número: '))
    quantidade += 1
    soma += numero
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    continuar = str(input('Deseja continuar?[S/n]: ')).upper().strip()[0]
    if continuar not in 'NS':
        print('Opção inválida')
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')