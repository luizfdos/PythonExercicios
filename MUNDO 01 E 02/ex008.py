# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e milímetros. Na aula ele pediu como extra km hm dam e dm
print('Conversor de Medidas')
n = float(input('Metros: '))
km = n / 1000
hm = n / 100 #hecametro
dam = n / 10 #decametro
dm = n * 10 #decimetro
cm = n * 100
mm = n * 1000
print(f"A medida de {n:.2f}m equivale a: \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm")
