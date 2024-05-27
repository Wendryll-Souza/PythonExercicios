'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol. na ordem de
colocação. Depois mostre:
- Apenas os 5 primeiros colocdos.
- Os ultimos 4 colocados.
- Uma lista com times em ordem alfabética.'''

times = ('Atletico-PR','Bahia','Flamengo','Botafogo','São Paulo','Cruzeiro','Atletico-MG','Bragantino','Palmeiras',
         'Internacional','Fortaleza','Grêmio','Vasco da Gama','Criciúma','Juventude','Corinthians','Fluminense',
         'Ec Vitória','Atletico-GO','Cuiabá')
times_ordenados =  sorted(times)

print('Tabela do Brasileirão')
for i in range(0,20):
    print(f'{i+1}° {times[i]}')

print('='*20)
print(f'Os cinco primeiros colocados da tabela: {times[:5]}')
print('='*20)
print(f'Os últimos 4 colocados da tabela: {times[-4:]}')
print('='*20)
print(f'Lista em ordem alfabetica: ')

for i in range(0,20):
    print(f'{i+1}º {times_ordenados[i]}.')