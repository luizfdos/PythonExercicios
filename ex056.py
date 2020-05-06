# DESAFIO 056 - DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
''' NO FINAL DO PROGRAMA, MOSTRE:
- A MEDIA DE IDADE DO GRUPO. ok
- QUAL É O NOME DO HOMEM MAIS VELHO.
- QUANTAS MULHERES TEM MENOS DE 20 ANOS. ok'''
mmenos20 = 0
somaidade = 0
nomemaisvelho = ''
idademaisvelho = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').upper().strip())
    somaidade += idade
    if sexo == 'M':
        if idade > idademaisvelho:
            idademaisvelho = idade
            nomemaisvelho = nome
    elif sexo == 'F':
        if idade < 20:
            mmenos20 += 1
mediaidade = somaidade / 4
print(f'A média das idades do grupo é de {mediaidade} anos.')
if idademaisvelho == 0:
    print('Não há homens no grupo.')
else:
    print(f'{nomemaisvelho.capitalize()} tem {idademaisvelho} anos e é o homem mais velho do grupo.')
if mmenos20 == 1:
    print(f'O grupo possui {mmenos20} mulher com menos de 20 anos')
elif mmenos20 > 1 or mmenos20 == 0:
    print(f'O grupo possui {mmenos20} mulheres com menos de 20 anos.')

# in 'Mm'