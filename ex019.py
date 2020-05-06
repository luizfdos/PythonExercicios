# DESAFIO 019 - UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE,
# LENDO E ESCREVENDO O NOME DO ESCOLHIDO
from random import choice
frase= "Escolha aluno"
print(41 * "-")
print(f"\n{frase:=^41}")
print("\n", 41 * "-")
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
lista = [aluno4, aluno3, aluno2, aluno1]
print(f"O aluno escolhido foi {choice(lista)}")