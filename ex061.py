times: tuple = ('Flamengo', 'Vasco da Gama', 'Atlético-MG', 'Palmeiras', 'São Paulo', 'Santos', 'Fluminense', 'Bahia',
        'Grêmio', 'Athletico-PR', 'Botafogo', 'Bragantino-SP', 'Internacional', 'Corinthians', 'Goiás', 'Fortaleza',
        'Atlético-GO', 'Sport Recife', 'Ceará SC', 'Coritiba')
#print(f'Lista de times: {times}')
print('=-'*15)
print('Lista de Times do Brasileirão')
print('=-'*15)
for t in times:
        print(t)
print(f'Os 5 primeiros times da tabela são: {times[0:5]}')
print(f'Os 4 últimos times da tabela são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}') # Ordedm alfabética da Tupla
print(f'Flamengo está na {times.index("Flamengo")+1}ª posição da tabela!')
