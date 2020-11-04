# DESAFIO 016 - FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂGULO
# RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
# A SOMA DOS QUADRADOS DOS CATETOS É IGUAL AO QUADRADO DA HIPOTENUSA (a² + b² = c²)

from math import hypot

print("Cálculo Hipotenusa" )
catoposto = float(input("Digite o cateto oposto: "))
catadjacente = float(input("Digite o cateto adjacente: "))
print(f"O comprimento da hipotenusa é {hypot(catoposto, catadjacente):.2f}")

'''print("Cálculo Hipotenusa")
catoposto = float(input("Digite o cateto oposto: "))
catadjacente = float(input("Digite o cateto adjacente: "))
print(f"O comprimento da hipotenusa é {(catoposto ** 2 + catadjacente ** 2) ** 0.5:.2f}")'''

'''from math import sqrt

print("Cálculo Hipotenusa")
catoposto = float(input("Digite o cateto oposto: "))
catadjacente = float(input("Digite o cateto adjacente: "))
print(f"O comprimento da hipotenusa é {sqrt(catadjacente ** 2 + catoposto ** 2):.2f}")'''

'''from math import sqrt,pow

print("Cálculo Hipotenusa")
catoposto = float(input("Digite o cateto oposto: "))
catadjacente = float(input("Digite o cateto adjacente: "))
print(f"O comprimento da hipotenusa é {sqrt(pow(catoposto,2) + pow(catadjacente,2)):.2f}")'''
