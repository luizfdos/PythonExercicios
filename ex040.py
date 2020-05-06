# DESAFIO - 040 - CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA,
# MOSTRANDO UMA MENSAGEM NO FINAL DE ACORDO COM A MÉDIA ATINGIDA:
# - MÉDIA ABAIXO DE 5.0: REPROVADO
# - MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# - MÉDIA 7.0 OU SUPERIOR: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2) / 2
if media >= 7:
    print(f"Sua média foi {media:.1f}. Você foi aprovado!")
elif media >= 5:
    print(f"Sua média foi {media:.1f}. Vocês está de recuperação!")
else:
    print(f"Sua média foi {media:.1f}Reprovado!")