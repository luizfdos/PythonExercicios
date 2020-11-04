# DESAFIO - 042 - REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR
# QUE TIPO DE TRIANGULO SERÁ FORMADO:
#   - EQUILÁTERO: TODOS OS LADOS IGUAIS
#   - ISÓSCELES: DOIS LADOS IGUAIS
#   - ESCALENO: TODOS OS LADOS DIFERENTES
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3+reta2 > reta1:
    print("As  podem formar um triângulo", end=' ')
    if reta1 == reta2 == reta3:
        print("EQUILATERO.")
    elif reta1 != reta2 != reta3 != reta1:
        print("ESCALENO!")
    else:
        print("ISÓCELES")
else:
    print("Essas três retas NÃO PODEM formar um triângulo")