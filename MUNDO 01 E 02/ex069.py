# DESAFIO 069 - CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. A CADA PESSOA CADASTRADA,
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTNUAR. NO FINAL, MOSTRE:
#
# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
# B) QUANTOS HOMENS FORAM CADASTRADOS.
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.
m20 = homens = mais18 = 0
sexo = ''
while True:
    print('-' * 40)
    print('           CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('Idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo in 'F' and idade < 20:
            m20 += 1
    if sexo in 'M':
        homens += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('============ FIM DO PROGRAMA ============')
print(f'Total de pessoas com de 18 anos ou mais: {mais18}')
print(f'Ao todo temos {homens} ', end='')
print('homem cadastrado' if homens == 1 else 'homens cadastrados')
print(f'E temos {m20} ', end='')
print('mulher com menos de 20 anos' if m20 == 1 else 'mulheres com menos de 20 anos')
