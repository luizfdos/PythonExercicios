# DESAFIO 050 - DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS
# DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O
soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i} número: '))
    if (numero % 2) == 0:
        soma += numero
        cont += 1
if cont == 1:
    print(f'Você informou apenas {cont} número par, o {soma}.')
elif cont > 1:
    print(f'Você informou {cont} números PARES, a soma é {soma}.')
else:
    print('Você não informou números PARES.')