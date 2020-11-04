# DESAFIO 038 - ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS,
# MOSTRANDO NA TELA UMA MENSAGEM:
# - O  PRIMEIRO VALOR É MAIOR
# - O SEGUNDO VALOR É MAIOR
# - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS
print("Digite dois valores para realizar a comparação.")
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print(f'O PRIMEIRO valor é maior! {valor1} > {valor2}')
elif valor2 > valor1:
    print(f'O SEGUNDO valor é maior! {valor2} > {valor1}')
else:
    print(f'Os dois valores são iguais.')
