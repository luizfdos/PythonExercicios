# DESAFIO 039 - FAÇA UM PROGRMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO
# COM SUA IDADE:
#   - SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
#   - SE É A HORA DE SE ALISTAR.
#   - SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
from datetime import date
ano = date.today().year
print(ano)
sexo = str(input('Você é:\n[ 1 ] - HOMEM\n[ 2 ] - MULHER\nOpção: '))
if sexo == '2':
    print('Você não precisa se alistar. O alistamento militar é obrigatório apenas para HOMENS.')
elif sexo == '1':
    nascimento = int(input('Digite o ano de seu nascimento:(ex:1990) '))
    idade = ano - nascimento
    print(f'Quem nasceu em {nascimento} completa {idade} anos em {ano}')
    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE!!")
    elif idade < 18:
        print(f"Ainda faltam {18 - idade} anos para seu alistamento. Você deverá se alistar em {(18-idade)+ano}. ")
    else:
        print(f'Você devia ter se alistado há {idade - 18} anos, seu alistamento foi em {ano - (idade - 18)}!')
else:
    print('Opção inválida! Você deve escolher [ 1 ] - HOMEM ou [ 2 ] - MULHER. Tente novamente.')


