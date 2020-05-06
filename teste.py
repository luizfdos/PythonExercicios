'''n = int(input("Digite o valor de n: "))
anterior = int(input("Digite um numero da sequencia: "))
i = 1  # i é contador de número lidos e já lemos o 1o número da sequência
while i < n:
    x = int(input("Digite um numero da sequencia: "))
    if x <= anterior:
        print("A sequencia nao esta ordenada")
    else:
        print("A sequencia esta ordenada")
    anterior = x
    i = i + 1'''

n = 6.875
print(f'{n:.2f}')
