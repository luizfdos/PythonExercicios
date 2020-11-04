# DESAFIO 077 -  CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS).
# DEPOIS DISSO, VOCÊ PODE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vowels = 'aeiou'

for word in words:
  print(f'\n Na palavra {word} temos ', end='')
  for letter in word:
    if letter in 'aeiouAEIOU':
      print(letter, end=' ')
