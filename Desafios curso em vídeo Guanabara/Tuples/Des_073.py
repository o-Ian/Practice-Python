tabela = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
          'Athletico-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza',
          'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Listas da tabela do Brasileirão: {tabela}')
print(f'Os primeiros cinco colocados da tabela: {tabela[0:5]}')
print(f'Os últimos 4 colocados: {tabela[16:]}')
print(f'Tabela em ordem alfabética: {sorted(tabela)}')
print('O Bahia está na {}ª posição' .format(tabela.index('Bahia')+1))
