# DESAFIO 024 - Crie um programa que leia o nome de uma cidade diga se ela
# começa ou não com o nome "SANTO".
cidade = input("Digite um nome de cidade: ").upper().strip().split()
print('O nome da cidade começa com SANTO?', 'SANTO' in cidade[0])
# print(cidade{:5}.upper() == 'SANTO')
