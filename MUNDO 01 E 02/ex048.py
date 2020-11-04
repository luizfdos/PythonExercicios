# DESAFIO 048 - FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES QUE SÃO
# MÚLTIPLOES DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.
soma = 0
contador = 0
for i in range(3, 501, 3):
    if i % 2 != 0:
        soma += i
        contador += 1
print(f'A soma dos {contador} valores solicitados é {soma}')
