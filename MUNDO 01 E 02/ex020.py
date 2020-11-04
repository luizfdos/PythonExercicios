# DESAFIO 020 - O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS
# ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.
from random import shuffle, sample

print("Digite o nome dos alunos para sortear a ordem de apresentação dos trabalhos")
aluno01 = input("Digite o nome do primeiro aluno: ")
aluno02 = input("Digite o nome do segundo aluno: ")
aluno03 = input("Digite o nome do terceiro aluno: ")
aluno04 = input("Digite o nome do quarto aluno: ")
lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)
print("A ordem de apresentação será", "\n")
print(lista)
'''sample = sample(lista, len(lista))
print("A ordem de apresentação será", "\n")
print(sample)'''
