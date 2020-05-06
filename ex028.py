# DESAFIO 027 - ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NUMERO DE
# 0 A 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO
# COMPUTADOR. O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USÁRIO VENCEU OU PERDEU.
from random import randint
from time import sleep
from termcolor import colored

def jogo():
    title = "ADIVINHAÇÃO"
    print(colored(20 * '-=-', 'yellow'))
    print(colored(f'{title:^60}', 'blue'))
    print(colored(20 * '-=-', 'yellow'))
    print(colored('Vou pensar em um número entre 0 e 5. Tente advinhar...', 'blue'))
    print(colored(20 * '-=-', 'yellow'))
    numero = randint(0,5)
    escolha = int(input("Em qual número estou pensando? "))
    print(colored('PROCESSANDO...', 'magenta'))
    sleep(1)
    if escolha == numero:
        print(colored(f"PARABÉNS! Você VENCEU! Eu estava pensando no numero {numero}!", 'green'))
        jogarnovamente()
    elif escolha != numero:
        print(colored(f"VOCÊ PERDEU! Eu pensei no número {numero} e não no {escolha}!", 'red'))
        jogarnovamente()

def jogarnovamente():
        escolha = str(input('Deseja jogar novamente?(S/N) '))
        if escolha.upper() == 'S':
            jogo()
        elif escolha.upper() == 'N':
            print(colored('Até a proxima!!', 'blue'))
            sleep(3)
            exit(0)
        else:
            print(colored('Opção inválida!!','red'))
            jogo()

jogo()