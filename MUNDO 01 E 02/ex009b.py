# DESAFIO 009 - Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
n = int(input('Digite o número do qual deseja saber a tabuada: '))
print('-' * 12)
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print(f"{n} x {3:2} = {n * 3}")
print(f"{n} x {4:2} = {n * 4}")
print(f"{n} x {5:2} = {n * 5}")
print(f"{n} x {6:2} = {n * 6}")
print(f"{n} x {7:2} = {n * 7}")
print(f"{n} x {8:2} = {n * 8}")
print(f"{n} x {9:2} = {n * 9}")
print(f"{n} x {10} = {n * 10}")
print('-' * 12)
