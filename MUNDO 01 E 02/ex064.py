# DESAFIO 064 - CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO.
# # O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO
# # DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA
# # ENTRE ELES (DESCONSIDERANDO O FLAG).
quantidade = 0
numero = int(input('Digite um número [999 para parar]: '))
soma = 0
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}')