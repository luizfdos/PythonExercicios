# DESAFIO 037 - ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL
# SERÁ A BASE DE CONVERSÃO:
# - 1 PARA BINÁRIO
# - 2 PARA OCTAL
# - 3 PARA HEXADECIMAL
numero = int(input("Digite um número inteiro: "))
opcao = str(input('Escolha uma base para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\nSua opção: '))
if opcao == '1':
    print(f'{numero} converido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opcao == '2':
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opcao == '3':
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida!')