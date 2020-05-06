# DESFIO 033 - FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR
numero1 = input()
numero2 = input()
numero3 = input()
maior = ''
menor = ''
lista = [numero1, numero2, numero3]
if numero2 > numero1 < numero3:
    menor = numero1
if numero2 < numero1 > numero3:
    maior = numero1
if numero3 > numero2 < numero1:
    menor = numero2
if numero3 < numero2 > numero1:
    maior = numero2
if numero1 > numero3 < numero2:
    menor = numero3
if numero1 < numero3 > numero2:
    maior = numero3
if maior != '' and menor != '':
    print(f' O menor valor digitador foi {menor}.\n O maior valor digitado foi {maior}.')
else:
    print("Você deve informar 3 valores DIFERENTES!")







'''print(min(lista))
print(max(lista))'''
