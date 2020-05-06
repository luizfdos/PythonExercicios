# DESAFIO 067 - FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, PARA CADA VALOR
# DIGITADO PELO USUÁRIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(30 * '-')
    if 0 > n:
        break
    for t in range(1, 11):
            print(f'{n} x {t:2} = {n * t}')
    print(30 * '-')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

