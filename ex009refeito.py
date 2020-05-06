'''inicial = 1
numero = int(input('Digite o número do qual deseja saber a tabuada: '))
limite = 10
while inicial <= limite:
    print(f"{numero} x {inicial:2} = {numero * inicial}")
    inicial += 1'''
m = 0
for i in range(1, 11):
    print(i, 'x', m, '=', i * (m + 1))