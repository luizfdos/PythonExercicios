# DESAFIO 054 - CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO
# FINAL MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES
from datetime import date

ano = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento: '))
    if ano - nascimento >= 21:
        maior += 1
    else:
        menor += 1
print(f'Pessoas que atingiram a maior idade: {maior}\nPessoas que não atingiram a maior idade: {menor}')
