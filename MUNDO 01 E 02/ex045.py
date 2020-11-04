# DESAFIO 045 - CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.
import os
from random import choice
from time import sleep


def jogar():
    print(f'\033[34m-=--=--=--=--PEDRA PAPEL OU TESOURA--=--=--=--=--=-')
    jokenpo = [1, 2, 3]
    escolhapc = str(choice(jokenpo))
    print('\033[0mESCOLHA UMA DAS OPÇÕES:\n[ 1 ] PEDRA\n[ 2 ] TESOURA\n[ 3 ] PAPEL')
    jogador = str(input("DIGITE O NÚMERO DA SUA ESCOLHA: "))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print(20 * '-=')
    if jogador == escolhapc:
        print(f'''\033[33mEmpate, vamos jogar novamente!\033[0:34m
REINICIANDO...''')
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        jogar()
    elif jogador == '1' and escolhapc == '2':
        print(f"Eu escolhi TESOURA\nVocê escolheu PEDRA\n\033[32mVocê venceu!\033[0m")
    elif jogador == '1' and escolhapc == '3':
        print(f"Eu escolhi PAPEL\nVocê escolheu PEDRA\n\033[31mVocê Perdeu!\033[0m")
    elif jogador == '2' and escolhapc == '3':
        print(f"Eu escolhi PAPEL\nVocê escolheu TESOURA\n\033[32mVocê venceu!\033[0m")
    elif jogador == '2' and escolhapc == '1':
        print(f"Eu escolhi PEDRA\nVocê escolheu TESOURA\n\033[31mVocê Perdeu!\033[0m")
    elif jogador == '3' and escolhapc == '1':
        print(f"Eu escolhi PEDRA\nVocê escolheu PAPEL\n\033[32mVocê venceu!\033[0m")
    elif jogador == '3' and escolhapc == '2':
        print(f"Eu escolhi TESOURA\nVocê escolheu PAPEL\n\033[31mVocê Perdeu!\033[0m")
    else:
        print('\033[31mOPÇÃO INVÁLIDA!\033[0m')
    print(20 * '-=')
    jogarnovamente()


def jogarnovamente():
    novamente = str(input("\033[0:33mDeseja jogar novamente?(S/N) \033[0m")).upper()
    if novamente == 'S':
        print("\033[34mOk, reiniciando...")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        jogar()
    elif novamente == 'N':
        print("Ok, até mais!")
    else:
        print("Opção inválida!")
        jogarnovamente()


jogar()
