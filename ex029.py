# DESAFIO - 029 - ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80Km/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.
from termcolor import colored
velocidade = int(input('Qual a velocidade do carro no momento?(KM/h) ').strip())
limite = 80
multa = (velocidade - limite) * 7
if velocidade <= limite:
    print(colored('Tudo ok! Até mais!', 'green'))
else:
    print(colored(f" Você foi multado! Você estava {velocidade-limite}KM/h acima do limite de {limite}KM/h. \n O valor da multa é de R${multa:.2f}!", 'red'))