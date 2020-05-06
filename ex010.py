# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos Dólares ela pode comprar. Considere US$ 1,00 = R$ 3,27
real = float(input('Quantos reais você tem na carteira? R$ '))
dolar = real / 4.15
euro = real / 4.62
yen = real / 0.038
print(f"Com R${real:.2f} você pode comprar: \nUS${dolar:^6.2f} \n  €{euro:.2f} \n  ¥{yen:.2f}")
