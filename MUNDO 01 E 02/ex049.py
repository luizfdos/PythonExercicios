# DESAFIO 049 - REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO
# ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
num = int(input('Digite o número do qual deseja saber a tabuada: '))
for i in range(1, 11):
    print(f'{num} x {i:2} = {i * num:2}')
