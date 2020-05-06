# DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A", em que posição ela aparece
# a primeira vez e em que posição ela aparece a última vez.
frase = input("Digite uma frase: ").lower().strip()
print(f"A frase possui {frase.count('a')} vezes a letra 'A'")
print(f"A letra 'A' aparece a primeira vez na posição {frase.find('a')+1}.")
print(f"A letra 'A' aparece pela ultima vez na posição {frase.rfind('a',)+1}.")