# DESAFIO 073 - CRIE UMA TUPLA PREENCHIDA COM OS  PRIMEIROS COLOCADOS DA TABELA DO 
# CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# A) APENAS OS 5 PRIMEIROS COLOCADOS.
# B) OS ÚLTIMOS 4 COLOCADOS DA TABLEA.
# C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
# D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DE CHAPECOENSE

times_brasileirao = ('Internacional', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo', 'Santos', 'Palmeiras', 'Grêmio', 'Sport', 'Fortaleza', 'Corinthians', 'Ceará', 'Atlético-GO', 'Botafogo', 'Bahia', 'Vasco', 'Coritiba', 'Bragantino', 'Athletico-PR', 'Goiás')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times_brasileirao}')
print('-=' * 30)
print(f'Os 5 primeiros são {times_brasileirao[:5]}')
print('-=' * 30)
print(f'Os 4 últimos são {times_brasileirao[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética {sorted(times_brasileirao)}')
print('-=' * 30)
print(f'O Chapecoense está na {times_brasileirao.index("Chapecoense")+1}ª posição' if 'Chapecoense' in times_brasileirao else f'O Chapecoense não está no Brasileirão')
