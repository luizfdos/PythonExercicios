# DESAFIO - 041 - A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA
# O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA DE ACORDO COM A IDADE:
#   - ATÉ 9 ANOS: MIRIM
#   - ATÉ 14 ANOS: INFANTIL
#   - ATÉ 19 ANOS: SÊNIOR
#   - ACIMA: MASTER
from datetime import date
print("---------------------------Categoria Natação----------------------------")
ano = date.today().year
anonascimento = int(input("Digite o ano de seu nascimento para saber a sua categoria(ex 1990): "))
idade = ano - anonascimento
print(idade)
if idade <= 9:
    print("CATEGORIA: MIRIM")
elif 9 < idade <= 14:
    print("CATEGORIA: INFANTIL")
elif idade <= 19:
    print("CATEGORIA: JUNIOR")
elif idade <= 25:
    print("CATEGORIA: SÊNIOR")
else:
    print("CATEGORIA: MASTER")