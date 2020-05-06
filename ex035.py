# DESAFIO 035 - DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA
# AO USUÁRIO SE ELES PODEM OU NÃO FORMAR UM TRIÂNGULO.,
reta1 = float(input("Digite a primeira reta: "))
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))
if reta1+reta2 > reta3 and reta1+reta3 > reta2 and reta2+reta3 > reta1:
    print("As três retas podem formar um triângulo.")
else:
    print("As três retas informadas NÃO podem formar um triângulo!")