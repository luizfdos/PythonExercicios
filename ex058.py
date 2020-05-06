# DESAFIO 058 - MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM
# NÚMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR,
# MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENDCER
from random import randint

print(20 * '\033[33m-=-\033[m')
print('{:^60}'.format('ADIVINHAÇÃO'))
print(20 * '\033[33m-=-')
print('\033[34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print(20 * '\033[33m-=-\033[m')
pc = randint(0, 10)
attempts = 1
user = int(input('Em qual número pensei? '))
while user != pc:
    if user > pc:
        user = int(input('Menos... Você errou, tente um novo número: '))
    elif user < pc:
        user = int(input('Mais... Você errou, tente um novo número: '))
    attempts += 1
print(f'Você acertou depois de {attempts} tentativas')
