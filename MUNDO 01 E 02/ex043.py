# DESAFIO - 043 - DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU
# IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
#   - ABAIXO DE 18.5: ABAIXO DO PESO
#   - ENTRE 18.5 E 25: PESO IDEAL
#   - 25 ATÉ 30: SOBREPESO
#   - 30 ATÉ 40: OBESIDADE
#   - ACIMA DE 40: OBESIDADE MÓRBIDA
print('{:=^40}'.format(' CÁLCULO IMC '))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print(f"{imc:.1f}")
if imc < 18.5:
    print(f"Sinto muito. Seu IMC é de {imc:.1f}, você está abaixo do peso. =(. Seu peso deveria ser no minímo")
elif 18.5 < imc <= 25:
    print(f"Parabéns! Seu IMC é {imc:.1f}, você está no seu peso ideal. =) ")
elif 25 <= imc <= 30:
    print(f"Sinto muito. Seu IMC é de {imc:.1f}, você está acima do peso. =(")
elif 30 < imc <= 40:
    print(f"Sinto muito. Seu IMC é de {imc:.2f}, você está obeso. =(")
else:
    print(f"Sinto muito. Seu IMC é de {imc:.2f}, você está com obesidade mórbida. =(")