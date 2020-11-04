# DESAFIO - 031 - DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM
# EM KM.CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ
# 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.#####################################
titulo = "PREÇO PASSAGEM"
def calculoviagem():
    print(f'{titulo:=^52}')
    dist_viagem = int(input('Qual a distância da viagem?(KM): '))
    if dist_viagem <= 200:
        print(f'O valor da passagem para essa viagem será: R${dist_viagem * 0.50:.2f}')
        print('=' * 52)
        calcularnovamente()
    else:
        print(f'O valor da passagem para essa viagem será: R${dist_viagem * 0.45:.2f}')
        print('=' * 52)
        calcularnovamente()

def calcularnovamente():
    resposta = input("Deseja fazer um novo cálculo?(s/N): ")
    if resposta.upper() == 'S':
        print("Ok!")
        calculoviagem()
    elif resposta.upper() == 'N':
        print("Ok! Até mais.")
        exit()
    else:
        print('Opção inválida, tente novamente!')
        calcularnovamente()
calculoviagem()


'''  
    preco = dist_viagem * 0.50 if dist_viagem <= 200 else dist_viagem * 0.45
    print(f'O valor da passagem para essa viagem será: R${preco:.2f}')
    print('=' * 52)
    calcularnovamente()'''