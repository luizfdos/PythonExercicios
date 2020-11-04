# DESAFIO 072 - CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA COM 
#  UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE
# SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXETENSO

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
  while True:
    typed = int(input('Digite um número entre 0 e 20: '))
    if 0 <= typed <= 20:
      break
    print('Tente novamente. ', end='')
  print(f'Você digitou o número {numbers[typed]}')
  continuar = str(input('Deseja continuar?(S/N) ')).upper().strip()[0]
  while continuar not in 'SN':
    continuar = str(input('Deseja continuar?(S/N) ')).upper().strip()[0]
  if continuar == 'N': 
    print('Até a próxima!')
    break



# typed = int(input('Digite um número entre 0 e 20: '))
# while typed < 0 or typed > 20:
#   typed = int(input('Tente novamente. Digite um número entre 0 e 20: '))

