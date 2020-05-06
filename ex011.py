# DESAFIO 011 - FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE
# A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA
# UMA ÁREA DE 2m².
print('Para saber a quantidade de tinta necessária para pintar a parede informe os dados a seguir: ')
larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
m2 = larg * alt
tinta = m2 / 2
print(f"Sua parede tem a dimensão de {larg:.2f}x{alt:.2f} e sua área é de {m2:.2f}m². \nVocê precisará de {tinta:.2f} lt de tinta para pintar a parede.")
