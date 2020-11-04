# DESAFIO 074 -  CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNCA COM NOMES DE PRODUTOS E SEUS 
# RESPECTIVOS PREÇOS, NA SEQUÊNCIA. 
# NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.

shoppingList = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90) 
print('-'*51)
print(f'{"LISTAGEM DE PREÇOS":^51}')
print('-'*51)
for i in range(0, len(shoppingList), 2): 
  print(f'{shoppingList[i]:.<40}', 'R$', f'{shoppingList[i+1]:>7.2f}')
print('-'*51)


