# DESAFIO 006 - Crie um algoritimo que leia um numero e mostre o seu dobro,
# triplo e raiz quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print("O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.".format(n, d, n, t, n, r))
#outra forma de fazer caso não precise guardar os resultados -
# print("O dobro de {} é {}. \nO triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.".format(n, (n*2), n, (n*3), n, (n**(1/2))))
