# DESAFIO - 034 - ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E
# CALCULE O VALOR DO SEU AUMENTO. PARA SALÁRIOS SUPERIORES A 1.250,00, CACLULE UM
# AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.
salario = float(input('Digite o valor do seu salário: R$'))
if salario <= 1250.00:
    aumento = 0.15*salario
    print(f'O seu salário terá um aumento de {aumento:.2f}(15%) e passará de R${salario:.2f} para R${salario+aumento:.2f}')
else:
    aumento = 0.10*salario
    print(f'O seu salário terá um aumento de {aumento:.2f}(10%) e passará de R${salario:.2f} para R${salario+aumento:.2f}')