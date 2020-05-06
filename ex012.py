# DESAFIO 012 - FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE
# DESCONTO
v = float(input('Qual o preço do produto? R$ '))
d = (v) - v * 0.05 #v - (v * 5 / 100)
print(f'O preço do produto com 5% de desconto é R${d:.2f}')
