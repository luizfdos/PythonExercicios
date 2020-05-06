# DESAFIO 021 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas ok
# O nome com todas as letras minúscula ok
# Quantas letras ao to.do sem considerar espaços ok
# Quantas letras tem o primeiro nome ok

nome = str(input("Digite seu nome completo: ")).strip()
print('Seu nome em maiúsculas é:', nome.upper())
print('Seu nome em minúsculas é', nome.lower())
print(f'Seu nome tem ao todo {len(nome)-nome.count(" ")} letras')
# print(f'Seu primeiro nome tem {nome.find(" ")} letras')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')
