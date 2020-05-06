# DESAFIO 013 - FAÇA UM ALGORITIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO, COM
# 15% DE AUMENTO.
s = float(input("Qual é o seu salário? "))
a = s * 0.15
ns = s + a
print(f"Seu salário terá um aumento de 15%(R$ {a:.2f}) e passará de R$ {s:.2f} para R$ {ns:.2f}.")
