# DESAFIO 018 - FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE
# ÂNGULO
from math import cos, sin, tan, radians
print("Calculo de seno, cosseno e tangente")
angulo = int((input("Digite o ângulo: ")))
angrad = radians(angulo)
seno = sin(angrad)
cosseno = cos(angrad)
tangente = tan(angrad)
print(f"O Ângulo de {angulo} tem:\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")
