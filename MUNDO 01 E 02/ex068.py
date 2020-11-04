# DESAFIO 068 - FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO
# QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
print('=-' * 20)
print('        VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
vitorias = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = jogador + computador
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if soma % 2 == 0:
        if opcao.strip() in 'Pp':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        else:
            break
    else:
        if opcao.strip() in 'Ii':
            print('Você VENCEU!\nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        else:
            break
if vitorias > 1:
    print(f'GAME OVER! Você venceu {vitorias} vezes.')
elif vitorias < 1:
    print(f'GAME OVER! Você não venceu nenhuma vez.')
else:
    print(f'GAME OVER! Você venceu 1 vez.')