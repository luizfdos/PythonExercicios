# DESAFIO 057 - FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES
# 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.
sexo = str(input('Informe seu sexo: [M/F] ').strip().upper()[0])
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0])
print(f'Sexo {sexo} registrado com sucesso.')
