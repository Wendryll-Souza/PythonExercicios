'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario.
No final, coloque esse dicionario em ordem. sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from operator import itemgetter


jogadores = dict()

print('Valores sorteados: ')
for i in range(1,5):
    numero = randint(1,6)
    print(f'O jogador {i} tirou {numero}')

    jogadores[f'Jogador{i}'] = numero

jogadores = sorted(jogadores.items(),key=itemgetter(1),reverse=True) # ordenando o dicionario

print('Ranking dos jogadores:')
for i in range(0,len(jogadores)):
    print(f'{i+1}º Lugar {jogadores[i][0]} com {jogadores[i][1]}')