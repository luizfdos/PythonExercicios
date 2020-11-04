# DESAFIO 053 - CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM
# PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.
'''EX: APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''
frase = input('Digite uma frase para verificar se ela é um palíndromo: ').upper().replace(' ', '')
invertido = frase[::-1]
if invertido == frase:
    print('A FRASE É UM PALÍNDROMO')
else:
    print('A FRASE NÃO É UM PALÍNDROMO')
