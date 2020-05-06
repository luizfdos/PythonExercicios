# DESAFIO 054 - FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL MOSTRE
# QUAL FOI O MAIOR E O MENOR PESO LIDOS.
lista = []
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    lista += [peso]
print(f'O maior peso lido foi de {max(lista)}Kg\nO menor peso lido foi de {min(lista)}Kg')